#!/usr/bin/env python
# encoding:utf-8
import time
import json
from loguru import logger
from flask import (g, request)
from app.errcode.code import *


class Decorator(object):
    def __init__(self, app, no_path):
        @app.before_request
        def before():
            g.start_time = time.time()

            if request.content_type == 'application/json;charset=UTF-8':
                g.payload = request.json
            else:
                payload = {}

                for k, v in request.values.to_dict().items():
                    payload[k] = v

                g.payload = json.dumps(payload, ensure_ascii=False)

            if "api/v1" in request.path and request.path not in no_path:
                if request.method == "POST":
                    token = request.headers.get("token")

                    from app import redis

                    if redis.exists(token) == 0:
                        return Response.code(ErrToken)

        @app.after_request
        def after_request(resp):
            response_data = ""
            try:
                response_data = resp.data
            except:
                pass

            log_data = {
                'method': request.method,
                'url': request.path,
                'request_id': request.headers.get('Requestid', ''),
                'headers': request.headers.to_wsgi_list(),
                'payload': g.payload,
                'code': resp.status_code,
                'elapsed_time': int((time.time() - g.start_time) * 1000),
                'response': response_data
            }

            logger.info(
                "{method} {url} {request_id} {code} {elapsed_time} {response}",
                url=log_data["url"],
                method=log_data["method"],
                request_id=log_data["request_id"],
                code=log_data["code"],
                elapsed_time=log_data["elapsed_time"],
                response=log_data["response"]
            )

            return resp

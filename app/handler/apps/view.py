#!/usr/bin/env python
# encoding:utf-8
from . import *


@route.route("/get/app/list", methods=['GET', 'POST'])
def get_app_list():
    if request.method == "GET":
        app_data = {}

        dir_list = File.find_apps(path=current_app.config["apps_path"])

        for d in dir_list:
            app_json = File.find_app_json(path=current_app.config["apps_path"], app_dir=d)

            app_d = json.loads(app_json)

            app_d["app_dir"] = d
            app_d["icon"] = d + "/icon.jpg"

            app_data[d] = app_d

        return Response.code(data=app_data)

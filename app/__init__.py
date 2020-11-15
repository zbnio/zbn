# !/usr/bin/env python
# encoding:utf-8
import os
import configparser
from loguru import logger
from flask_cors import CORS
from flask_orator import Orator
from flask_redis import FlaskRedis
from flask_sockets import Sockets
from app.handler import Decorator
from flask import (Flask, send_from_directory)

db = Orator()
redis = FlaskRedis()
sockets = Sockets()

def reg_log(app):
    
    base = app.config['project_path'] + "/log"

    info_path = os.path.join(base, 'info.{time:YYYY-MM-DD}.log')
    error_path = os.path.join(base, 'error.{time:YYYY-MM-DD}.log')

    logger.remove()

    logger_format = "{time:YYYY-MM-DD HH:mm:ss,SSS} [{thread}] {level} {file} {line} - {message}"

    logger.add(info_path, format=logger_format, enqueue=True, rotation="00:00", retention='10 days',
               encoding='utf-8',level='INFO')

    logger.add(error_path, format=logger_format, enqueue=True, rotation="00:00", retention='10 days',
               encoding='utf-8', level='ERROR')

def reg_route(app):
    from app.handler.login import route as route_login
    from app.handler.user import route as route_user
    from app.handler.type import route as route_type
    from app.handler.variablen import route as route_variablen
    from app.handler.system import route as route_system
    from app.handler.apps import route as route_apps
    from app.handler.workflow import route as route_workflow
    from app.handler.logs import route as route_logs
    from app.handler.dashboard import route as route_dashboard

    from app.handler.workflow import ws as ws_workflow

    route_list = [route_login, route_user, route_type, route_variablen, route_system, route_apps, route_workflow,
                  route_logs, route_dashboard]

    for route in route_list:
        app.register_blueprint(route, url_prefix="/api/v1")

    sockets.register_blueprint(ws_workflow, url_prefix=r'/')


def reg_vue(app):
    @app.route('/')
    def index():
        return start.send_static_file('index.html')

    @app.route('/<path:file>')
    def route(file):
        return app.send_static_file(file)


def reg_plug(app):
    @app.route('/app/<path:file>')
    def app_icon(file):
        file_arr = str(file).split("/")

        file_name = file_arr[1]

        file_path = app.config['project_path'] + "/app/core/apps/" + file_arr[0]

        return send_from_directory(directory=file_path, filename=file_name)


def reg_config(app):
    app.config['project_path'] = os.getcwd()
    app.config['apps_path'] = app.config['project_path'] + "/app/core/apps"

    cf = configparser.ConfigParser()
    cf.read(app.config['project_path'] + '/config.ini')

    app.config['ORATOR_DATABASES'] = {
        'development': {
            'driver': 'mysql',
            'host': cf.get("mysql", "host"),
            'port': int(cf.get("mysql", "port")),
            'database': cf.get("mysql", "database"),
            'user': cf.get("mysql", "user"),
            'password': cf.get("mysql", "password")
        }
    }

    redis_host = cf.get("redis", "host")
    redis_port = cf.get("redis", "port")
    redis_database = cf.get("redis", "database")
    redis_password = cf.get("redis", "password")

    if str(redis_password) == "":
        app.config['REDIS_URL'] = "redis://{host}:{port}/{db}".format(
            host=redis_host,
            port=redis_port,
            db=redis_database
        )
    else:
        app.config['REDIS_URL'] = "redis://:{password}@{host}:{port}/{db}".format(
            password=redis_password,
            host=redis_host,
            port=redis_port,
            db=redis_database
        )


def reg_db(app):
    db.init_app(app=app)
    redis.init_app(app=app)


def reg_cors(app):
    CORS(
        app=app,
        resources={
            r"/api/*": {"origins": "*"},
            r"/app/*": {"origins": "*"}
        }
    )


def reg_decorator(app):
    no_path = [
        "/api/v1/login",
    ]

    Decorator(app=app, no_path=no_path)


def reg_web_sockets(app):
    sockets.init_app(app=app)


def create_app():
    app = Flask(__name__, static_folder='html')

    reg_config(app=app)
    reg_log(app=app)
    reg_cors(app=app)
    reg_db(app=app)
    reg_vue(app=app)
    reg_plug(app=app)
    reg_route(app=app)
    reg_decorator(app=app)
    reg_web_sockets(app=app)

    app.app_context().push()

    return app


start = create_app()

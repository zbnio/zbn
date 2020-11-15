#!/usr/bin/env python
# encoding:utf-8
from app import start
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler


def print_info(**kwargs):
    print("  ____  ____  __ _    ____   __    __   ____ ")
    print(" (__  )(  _ \(  ( \  / ___) /  \  / _\ (  _ \\")
    print("  / _/  ) _ (/    /  \___ \(  O )/    \ )   /")
    print(" (____)(____/\_)__)  (____/ \__/ \_/\_/(__\_) v0.1")
    print("")
    print("* Welcome to ZBN SOAR service")
    print("===========================")
    print("* Web : https://zbn.io")
    print("* Github : https://github.com/zbnio/zbn")
    print("===========================")
    print("* Running on http://{host}:{port}/ (Press CTRL+C to quit)".format(host=kwargs["host"], port=kwargs["port"]))


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8888

    print_info(host=host, port=port)

    server = pywsgi.WSGIServer((host, port), start, handler_class=WebSocketHandler)
    server.serve_forever()

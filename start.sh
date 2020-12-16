#!/bin/bash

# -w 是进程数
# -t 是线程数


gunicorn  -w 2 -t 3 --timeout 5 app:start -b 0.0.0.0:8888

from flask import Blueprint
from loguru import logger
from app import (db, redis)
from app.errcode.code import *
from app.utils.times import Time
from app.utils.randoms import Random
from flask import (request, current_app)
import json
import platform

if platform.system() == 'Windows':
    from app.core.windows.core import run_exec
elif platform.system() == 'Linux':
    from app.core.linux.core import run_exec
elif platform.system() == "Darwin":
    from app.core.mac.core import run_exec

route = Blueprint('workflow', __name__)
ws = Blueprint(r'ws', __name__)

from . import view

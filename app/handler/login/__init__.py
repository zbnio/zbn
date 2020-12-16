from flask import Blueprint
from loguru import logger
from app import (db, redis)
from app.errcode.code import *
from app.utils.times import Time
from app.utils.randoms import Random
from flask import (request, current_app)

route = Blueprint('login', __name__)

from . import view

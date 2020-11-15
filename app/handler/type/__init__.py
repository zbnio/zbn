from flask import Blueprint
from loguru import logger
from app import db
from app.errcode.code import *
from app.utils.times import Time
from flask import (request, current_app)

route = Blueprint('type', __name__)

from . import view

from flask import Blueprint

# 1. 创建蓝图对象
# home_blu = Blueprint("home_b",__name__,url_prefix="/home")
#
# @home_blu.before_request
# def home_prepare():
#     print("before_request")
users_bp = Blueprint("users_bp",__name__,url_prefix="/home")
from . import views







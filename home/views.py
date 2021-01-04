from home import users_bp
from flask import url_for
# 2. 使用蓝图对象来定义路由
@users_bp.route("/users")
def get_profile():
    return "users blueprint module"

@users_bp.route("/demo")
def demo():
    url1 = url_for("home_b.demo")
    print(url1)
    return "demo"


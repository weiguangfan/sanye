from flask import Flask,request,Response,make_response,jsonify,redirect,session,abort,current_app,g
from werkzeug.routing import BaseConverter
from werkzeug.datastructures import FileStorage
from datetime import timedelta
from home import users_bp
import tool
from functools import wraps

# 1.创建Flask应用
app = Flask(__name__)
# 3.应用注册蓝图对象
app.register_blueprint(users_bp)
app.secret_key = "test"
# 1.定义转换器类
# class MobileConverter(BaseConverter):
#     # 2.设置regex属性(匹配规则)
#     regex = '1[3-9]\d{9}$'  # 不要设置开头的^

# 3.添加自定义转换器
# app.url_map.converters['mob'] = MobileConverter

# 每次执行视图函数之前调用, 对请求进行一些准备处理, 如参数解析, 黑名单过滤, 数据统计等
@app.before_request
def prepare():
    # 必须使用g变量来传递数据, 使用全局变量不能记录并发的多个请求数据
    g.name = session.get("username")


# 每次执行视图函数之后(已经包装为响应对象)调用, 对响应进行一些加工处理, 如设置统一响应头, 设置数据的外层包装
# @app.after_request
# def process(response:Response):  # 必须定义形参接收响应对象
#     print('after_request:')
#     # print(response.headers)
#     # print(response.data)
#     # print(response.status_code)
#     return response

# web应用被第一次请求前调用, 可以进行web应用初始化处理, 如数据库连接
# @app.before_first_request
# def initial():
#     print('before_first_request')


# 每次执行视图函数之后调用, 无论是否出现异常都会执行, 一般用于请求收尾, 如资源回收, 异常统计
# @app.teardown_request  # 测试时不要开启调试模式
# def request_handle(error):  # 必须定义形参来接收具体错误信息, 如果没有错误, error=None
#     print('teardown_request : %s' % error)


# 捕获http错误
# @app.errorhandler(404)
# def error_404(error):  # 一旦进行捕获, 要求必须定义形参接收具体错误信息
#     return "<h3>您访问的页面去浪迹天涯了</h3> %s" % error

# 还可以捕获系统内置错误
# @app.errorhandler(ZeroDivisionError)
# def error_zero(error):
#     return '除数不能为0'


# @app.route('/hello', methods=['post', 'get'])
# def hello():
#     return jsonify(name="zs",age=30)


# 3.定义路由
@app.route('/', methods=['post', 'get'])
def index():
    # return "index page"
    # print(userid)
    # 获取请求的基础数据
    # print(request.url)  # 请求的URL
    # print(request.method)  # 本次请求的请求方式
    # print(request.headers)  # 获取请求头信息  类字典对象

    # print(request.headers['Host'])
    # print(request.headers.get('Host'))  # 建议使用get方法, 键不存在不报错

    # 请求传递数据
    # 1> URL路径 -> 路由变量
    # 2> 查询字符串 get
    # 3> 请求体  post
    # 4> 请求头 -> request.headers

    # 获取查询字符串 -> request.args  xx?name=zs&age=20  类字典对象
    # print(request.args.get('name'))
    # print(request.args.get('age'))

    # 请求体:   键值对(表单)   文本(json/xml)  文件(图片/音频)

    # 获取post键值对 -> request.form  类字典对象
    # print(request.form.get('address'))

    # 获取post文本数据 -> request.data / request.json
    # print(request.data)  # 返回bytes类型
    # print(request.json.get('age'))  # request.json直接将json字符串转为字典

    # 获取post文件 -> request.files  类字典对象
    # file = request.files.get("address")  # type: FileStorage
    # print(type(file))  # 返回 FileStorage文件对象
    # 将文件保存到本地
    # file.save('./static/123.jpg')

    # 获取文件的二进制数据
    # img_bytes = file.read()
    # print(img_bytes)

    # 返回值:  响应体, 响应状态码, 响应头
    # return 'demo1', 400, {'A': 40}
    # return 'hello flask 2020'

    # 视图函数的返回值可以为str/bytes类型, 并且flask内部会将其包装为Response响应对象
    # return 'hello flask'

    # 创建响应对象     设置响应头时,需要手动创建响应对象
    # response = make_response('hello flask')  # type: Response
    # 设置响应头
    # response.headers['B'] = 10
    # return response
    # dict1 = {'name': 'zs', 'age': 20}
    # 字典转json字符串
    # return json.dumps(dict1)

    # 可以将字典转json字符串, 并且设置响应头的content-type为application/json
    # return jsonify(dict1)
    # return jsonify(name='zs', age=20)  # 也支持关键字实参的形式

    # 重定向到指定网站
    # return redirect('http://www.baidu.com')
    # 重定向到自己的路由   只需要URL资源段
    # return redirect('/hello')

    # 后端设置cookie:  通过响应体的set_cookie字段

    # 创建响应对象
    # response = make_response('hello flask 2021')  # type: Response

    # 设置响应头的set_cookie字段  value必须是str/bytes类型
    # response.set_cookie('per_page', '10', max_age=86400)

    # 删除cookie   本质: 设置max-age=0
    # response.delete_cookie('per_page')

    # 获取cookie:  浏览器会自动通过请求头的cookie字段来传递cookie数据

    # request.cookies 直接获取到字典形式的cookie数据
    # print(request.cookies.get('per_page'))

    # 设置应用秘钥   会被用于session签名
    # app.secret_key = 'test'
    # 设置session过期时间   默认31天
    # app.permanent_session_lifetime = timedelta(days=7)
    # session是一个类字典对象, 对其取值/赋值 就可以实现session数据的读写

    # 记录session数据
    # session['username'] = 'ls'

    # 设置session支持过期时间
    # session.permanent = True

    # 获取session数据
    # name = session.get('username')
    # print(name)
    # 删除session数据
    # session.pop('username')
    # print('执行视图')
    # a = 1 / 0
    # abort(500)  # 主动抛出异常 (只能抛出http错误)

    # g.name = "zs"
    # tool.func1()
    # return "index"
    if g.name:
        return "欢迎回来, %s" % g.name
    else:
        return '首页'
    # return "hello flask 2021"

@app.route("/demo")
def demo():
    print(g.name)
    return "demo"

@app.route('/login')
def login():
    """登录"""
    session['username'] = 'zs'
    return '登录成功'

# 需求2: 对部分视图进行访问限制  如个人中心必须登录才能访问
# 解决方案: 使用装饰器封装访问限制   减少代码冗余
def login_required(f):  # f = user
    @wraps(f)
    def wrapper(*args, **kwargs):
        # 获取函数名
        print(wrapper.__name__)
        if g.name:  # 用户已登录
            return f(*args, **kwargs)  # 正常访问视图函数
        else:  # 用户未登录
            abort(401)  # 400 语法/参数错误 401 未认证  403 已认证, 权限不足  404 资源不存在  405 请求方式不支持  500 服务器错误
    return wrapper

@app.route('/user')
@login_required  # user = login_required(user)
def user():
    """个人中心"""
    return '访问 %s 的个人中心' % g.name

@app.route("/demo1")
@login_required
def demo1():
    return "demo1"



    # --------- project  # 工程目录
    # | ------ main.py  # 启动文件
    # | ------ user  # 用户模块
    # | | --- __init__.py  # 包的初始化文件, 此处创建管理用户模块的蓝图对象
    # | | --- views.py  # 视图文件
    # | | --- ...
    # |
    # | ------ home  # 首页模块
    # | | --- __init__.py  # 包的初始化文件, 此处创建管理首页模块的蓝图对象
    # | | --- views.py  # 视图文件
    # | | --- ...
    # | ...


if __name__ == '__main__':
    # 2.运行应用 (启动一个测试服务器, 接收请求并调用对应的视图函数)
    # app.run()
    # host: 绑定的ip(域名)  0.0.0.0
    # port: 监听的端口号
    # debug: 是否开启调试模式  1> 可以在网页上显示python错误 2> 更新代码后测试服务器自动重启
    # 获取路由信息
    print(app.url_map)
    app.run()
    # for rule in app.url_map.iter_rules():
    #     print(rule.rule, rule.methods, rule.endpoint)
    # app.run(host='0.0.0.0', port=8000, debug=True)


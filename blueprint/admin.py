# 处理后台业务蓝图
from flask import Blueprint, render_template, request, make_response, jsonify

from exts import db
from forms import RegisterForm
from models import UserModel
from werkzeug.security import generate_password_hash, check_password_hash

from token_identify import get_token

# 处理后台业务
bp = Blueprint("admin", __name__, url_prefix="/admin")


# 后台首页 /admin/index
@bp.route('/index')
def admin_index():
    return render_template("admin/index.html")


# 登录跳转 /login
@bp.route('/login')
def admin_login():
    return render_template("admin/login.html")


# 跳转注册界面方法
@bp.route('/reg')
def reg():
    return render_template("admin/reg.html")


# 注册用户接口
@bp.route('/regSave', methods=['POST'])
def regSave():
    # 验证表单信息
    forms = RegisterForm(request.form)
    if forms.validate():
        # 验证成功
        # 获取表单数据
        email = forms.email.data
        username = forms.username.data
        password = forms.password.data
        tel = forms.tel.data
        # 封装Model数据
        user = UserModel(username=username, password=generate_password_hash(password), email=email, tel=tel)
        # 保存数据到数据库
        db.session.add(user)
        db.session.commit()

        return {
            "isSuccess": True,
            "msg": "注册成功"
        }
        pass
    else:
        # 验证失败
        err_msg = ''
        for k, v in forms.errors.items():
            err_msg = err_msg + v[0]
        response = make_response(jsonify({
            "isSuccess": False,
            "msg": err_msg
        }))
        return response


# 登录校验接口
@bp.route('/login/checkLogin', methods=['POST'])
def checkLogin():
    # 获取表单数据
    username = request.values.get('username')
    password = request.values.get('password')

    # 查看数据库
    user = UserModel.query.filter_by(username=username).first()
    if not user:
        return {
            "isSuccess": False,
            "msg": "用户不存在"
        }
    if check_password_hash(user.password, password):
        return {
            "isSuccess": True
        }
    else:
        return {
            "isSuccess": False,
            "msg": "密码错误"
        }
        pass


# 获取token
@bp.route('/token', methods=['GET'])
def get_token():
    username = request.values.get('username')
    pwd = request.values.get('secret')
    access_token = get_token(username)
    return {
        "access_token": access_token,
        "expires_in": 1800
    }

import pymysql
from flask import Flask, jsonify, request, make_response
import jwt
import datetime
import config
from exts import db
from flask_migrate import Migrate
from blueprint.admin import bp as admin_bp

# 假设我们有一个简单的用户数据字典存储实际token信息
users = {"123": {"username": "admin", "password": "secret"}}

# 数据库链接信息
db_config = {"host": "localhost",  # MySQL服务器地址
             "user": "root",  # 用户名
             "password": "123456",  # 密码
             "database": "study"  # 数据库名称
             }

# 获得Flask实例类 做web应用 通过浏览器访问到flask服务
app = Flask(__name__)

# 数据库链接操作
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)

# 注册蓝图
app.register_blueprint(admin_bp)

# Secret key for signing JWT
# SECRET_KEY = "your_secret_key"
#
#
# def authenticate(username, password):
#     db_conn = pymysql.connect(**db_config)
#     cursor = db_conn.cursor()
#     query_user_sql = "select * from db_account where username=%s and password=%s"
#     cursor.execute(query_user_sql, (username, password))
#     result = cursor.fetchall()
#     if result:
#         return True
#     else:
#         return False


# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     if authenticate(data['username'], data['password']):
#         exp_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=30)  # 设置 token 过期时间为30分钟
#         payload = {'user_id': data['username'], 'exp': exp_time}
#
#         access_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
#
#         # 返回包含 token 的响应
#         response = make_response(jsonify({'access_token': access_token}))
#         response.headers.add('Content-Type', 'application/json')
#         response.headers['Authorization'] = f"Bearer {access_token}"
#         return response, 200
#     else:
#         return make_response(jsonify({'error': 'Invalid credentials'})), 401


if __name__ == '__main__':
    app.run(debug=True)

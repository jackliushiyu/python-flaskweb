# Secret key for signing JWT
import datetime

import jwt

SECRET_KEY = "your_secret_key"


# 通过用户名和时间获取token
def get_token(username):
    exp_time = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=30)  # 设置 token 过期时间为30分钟
    payload = {'user_id': username, 'exp': exp_time}

    access_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return access_token


# 校验token
def token_identify(token):
    pass

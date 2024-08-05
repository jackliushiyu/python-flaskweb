# 数据库链接信息
import datetime

import pymysql

db_config = {"host": "localhost",  # MySQL服务器地址
             "user": "root",  # 用户名
             "password": "123456",  # 密码
             "database": "study"  # 数据库名称
             }


def authenticate(username, password):
    db_conn = pymysql.connect(**db_config)
    cursor = db_conn.cursor()
    query_user_sql = "select * from db_account where username=%s and password=%s"
    cursor.execute(query_user_sql, (username, password))
    result = cursor.fetchall()
    if result:
        print(result)
    else:
        print(False)


if __name__ == "__main__":
    # authenticate("admin", "$2a$10$IHZ.9wHHYHBO8CP3VUS6WOLfMMo8Hie2kjnZ7aYbY68hgiUpwdDL6")
    print(datetime.datetime.now(datetime.UTC))
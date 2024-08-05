from exts import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = "db_account"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    tel = db.Column(db.String(11), unique=True)
    create_time = db.Column(db.DateTime, default=datetime.now)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "tel": self.tel,
            "password": self.password,
            "create_time": self.create_time
        }


if __name__ == "__main__":
    user = UserModel.query.filter_by(email="111@qq.com")
    print(user)

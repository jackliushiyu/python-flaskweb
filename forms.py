import wtforms
from wtforms.validators import Email, Length
from models import UserModel


class RegisterForm(wtforms.Form):
    # 验证格式
    email = wtforms.StringField(validators=[Email(message="邮箱格式出错")])
    username = wtforms.StringField(validators=[Length(min=4, max=20, message="用户名长度应在4-20")])
    password = wtforms.StringField(validators=[Length(min=4, max=20, message="密码长度应在4-20")])
    tel = wtforms.StringField(validators=[Length(min=11, max=11, message="密码长度应为11位数")])

    def validate_email(self, field):
        email = field.data
        # 查询数据库 邮箱是否重复
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.validators.ValidationError(message="邮箱重复了")

    def validate_username(self, field):
        username = field.data
        # 查询数据库 邮箱是否重复
        user = UserModel.query.filter_by(username=username).first()
        if user:
            raise wtforms.validators.ValidationError(message="用户已存在")

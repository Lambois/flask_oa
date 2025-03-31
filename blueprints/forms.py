import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired
from models import UserModel
from exts import db,r

class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    captcha = wtforms.StringField(validators=[Length(max=4, min=4, message="验证码格式错误")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="用户格式错误")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message="两次密码不一致")])

    # 自定义验证
    # 1、 邮箱是否被注册
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已经被注册！")

    # 2、 验证码是否正确

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        # filters = {'email': email, 'captcha': captcha}
        # captcha_model = EmailCaptchaModel.query.filter_by(**filters).first()
        captcha_ext = r.exists(email)
        
        # print(email,captcha,captcha_model.email)
        if not captcha_ext:
            raise wtforms.ValidationError(message="邮箱错误")
        # tode 可以删除 captcha_model
        else:
            if r.get(email).decode() != captcha:
                raise wtforms.ValidationError(message="验证码错误")
            else:
                r.delete(email)
            # 使用完毕可以删除 或者 定义是否使用  # False是0,true是1
            # db.session.delete(captcha_model)
            # db.session.commit()
            # captcha_model.used = 1
            # db.session.commit()

        
class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])

class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="标题格式错误")])
    content = wtforms.StringField(validators=[Length(min=3, message="密码格式错误")])

class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, message="密码格式错误")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="必须传入问题id!")])


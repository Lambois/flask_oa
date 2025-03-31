from flask import Blueprint,render_template,url_for,redirect,session
from exts import mail,r,db
from flask_mail import Message
from flask import request
import string,random
import h_json
from .forms import RegisterForm,LoginForm
from models import UserModel
from werkzeug.security import generate_password_hash,check_password_hash

bp = Blueprint("auth",__name__,url_prefix='/auth')

# @bp.route('/login')
# def login():
#     pass

# @bp.route('/register')
# def register():
#     return render_template('register.html')
#     # return 'hahahaha'


@bp.route("/login",methods = ['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.data['email']
            password = form.data['password']
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱不存在")
                return redirect(url_for('auth.login'))
            else:
                if check_password_hash(user.password,password):
                    session['user_id'] = user.id
                    return redirect("/")
                else:
                    print('密码错误')
                    return redirect(url_for('auth.login'))
        else:
            print(form.errors)
            return redirect(url_for('auth.login'))

# 注销
@bp.route('/logout/')
def logout():
    session.clear()
    return redirect("/")


# GET :从服务获取数据
# POSt ：将客户端的数据提交个服务器
@bp.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.data["email"]
            username = form.data["username"]
            password = form.data["password"]
            user = UserModel(email=email,username=username,password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            print(form.errors)
            return redirect(url_for('auth.register'))

def send_async_email(app, msg):
    # with app.app_context():
    #     mail.send(msg)
    pass


# 邮箱的验证码
@bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get('email')
    str_ = (string.digits+string.ascii_lowercase+string.ascii_uppercase)*4
    captcha = random.sample(str_,4)
    # print(captcha)
    captcha = ''.join(captcha)
    r.setex(email,60,captcha)
    message = Message(subject='验证码',recipients=[email],body=f'{captcha}')
    mail.send(message)
    mail_json = h_json.Json(200,"",None)
    return mail_json.h_jsonify()



@bp.route("/mail/test")
def mail_test():
    message = Message(subject='邮箱测试',recipients=['782269694@qq.com'],body='这是一条测试邮件')
    mail.send(message)
    return '邮箱发送成功'

@bp.route("/redis/test")
def redis_test():
    s_ = r.keys('*')
    print(s_)
    return "测试成功"

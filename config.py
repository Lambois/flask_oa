SECRET_KEY = "sadhjiohasda.sd;'as.dk"

HOSTNAME = "127.0.0.1"

PORT = "3306"

USERNAME = "root"

PASSWORD = "123456"

DATABASE = "oa"

DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'

SQLALCHEMY_DATABASE_URI = DB_URL

#taxrdruoifxcbdfg

# 邮箱地址
MAIL_SERVER = 'smtp.qq.com'
MAIL_PROT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "你自己的邮箱地址"
MAIL_PASSWORD = "邮箱smtp服务的放行码"
MAIL_DEFAULT_SENDER = "你自己的邮箱地址"
# MAIL_DEBUG = True
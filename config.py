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
MAIL_USERNAME = "782269694@qq.com"
MAIL_PASSWORD = "taxrdruoifxcbdfg"
MAIL_DEFAULT_SENDER = "782269694@qq.com"
# MAIL_DEBUG = True
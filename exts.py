from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import redis

db = SQLAlchemy()
mail = Mail()

pool = redis.ConnectionPool(host='127.0.0.1',port = 6379)
r = redis.Redis(connection_pool=pool)
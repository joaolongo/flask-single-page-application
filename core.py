import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    SECRET_KEY = 'my_precious'
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ceres#2018@192.168.33.10/les1819'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://jgmiranda:LH4h63jhNQQg@jgmiranda.mysql.pythonanywhere-services.com/jgmiranda$bolao'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

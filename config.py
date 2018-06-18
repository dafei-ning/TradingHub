# config

# pylint: disable=invalid-name, too-few-public-methods

class Config:
    """config"""
    SECRET_KEY = ''

    # 数据库设置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 邮件设置
    FLASKY_MAIL_SUBJECT_PREFIX = '[SVInsight Sister]'
    FLASKY_MAIL_SENDER = ''
    FLASKY_ADMIN = ''

    API_KEY = "key"

    # 表单保护
    API_SECRET = "Secret" 

    @staticmethod
    def init_app(app):
        """pass"""
        pass


class DevelopmentConfig(Config):
    """Dev"""
    DEBUG = True

    # 邮件设置
    MAIL_SERVER = ''
    MAIL_PORT = 
    MAIL_USE_TLS = 
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''

    # 数据库地址设置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://数据库用户名:密码@地址:3306/数据库名'


class TestingConfig(Config):
    """test"""
    TESTING = True

class ProductionConfig(Config):
    """production"""


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
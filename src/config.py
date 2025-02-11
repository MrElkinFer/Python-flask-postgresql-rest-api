from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')


class DepelomentConfig(Config):
    DEBUG = True


configKey = {
    'development': DepelomentConfig
}

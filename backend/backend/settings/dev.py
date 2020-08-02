from .common import *

INSTALLED_APPS += [
    'debug_toolbar',
]

# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]
# 이렇게 설정하면 미들웨어 제일 마지막에 추가가 된다

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE
# 이렇게 해야 미들웨어의 처음에 추가가 된다

INTERNAL_IPS = ['127.0.0.1']

CORS_ORIGIN_WHITELIST = ["http://localhost:3000"]

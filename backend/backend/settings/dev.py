from .common import *

# debug_toolbar같은 경우에는 개발시에만 쓰이므로 이렇게 개발 관련된 환경에만 추가해준다!


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
# debug_toolbar를 허용할 IP의 목록을 설정

CORS_ORIGIN_WHITELIST = ["http://localhost:3000"]
# 장고 서버로 ajax 요청시에 호스트 명이 다를 경우 보안 정책상 요청을 거절한다
# 장고가 서비스되는 호스트명은 http://localhost:8000이고 리액트는 http://localhost:3000이기 때문에 요청이 안됨!
# 이렇게 호스트명이 다를 시에 cors headers를 이용하여 접근을 허용해준다
# 위의 경우 http://localhost:3000을 허락한다는 뜻

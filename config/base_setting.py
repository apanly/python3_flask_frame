# -*- coding: utf-8 -*-
APP_NAME = "python3_flask_frame"
APP_VERSION = "V1.0"
SERVER_PORT = 8889
API_SERVER_PORT = 8888

'''
有可能你使用浏览器看到的一串字符串(ascii编码)不是那么容易看懂的，
这是因为python底层使用unicode编码。
通过设置下面的参数可以解决这个问题。
'''
JSON_AS_ASCII = False


DEBUG = False
DEBUG_TB_INTERCEPT_REDIRECTS = False
SQLALCHEMY_ECHO = False
SECRET_KEY = 'ZoDWffA2deeVOzii'

## 域名配置
DOMAIN = {
    "www": "http://192.168.33.10:8889",
    "api": "http://192.168.33.10:8888",
}


##过滤url
IGNORE_URLS = [
    "^/user/login",
    "^/user/logout",
]

##登录忽略url
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

##HTTP请求超时时间
HTTP_TIMEOUT = 5

##日志存放位置
LOG_ROOT_PATH = "/data/logs/python3_flask_frame"
##版本号文件
RELEASE_PATH = "/data/www/release_version/python3_flask_frame"


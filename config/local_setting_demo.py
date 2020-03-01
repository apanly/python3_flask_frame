# -*- coding: utf-8 -*-
'''
修改文件名为local_setting.py，然后作为本地开发配置
'''
from config.base_setting import *
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1/python3_flask_frame'

SQLALCHEMY_ENCODING = "utf-8"


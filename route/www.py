# -*- coding: utf-8 -*-
'''
专门为web程序准备的初始化入口
'''
from application import app

'''
toolbar
'''

# from flask_debugtoolbar import DebugToolbarExtension
# toolbar = DebugToolbarExtension(app)


'''
统一拦截处理和统一错误处理
'''

from web.interceptors.Auth import  *
from web.interceptors.ErrorHandler import  *


'''
蓝图功能，对所有的url进行蓝图功能配置
'''
from web.controllers.index import route_index
from web.controllers.static import route_static
from web.controllers.user.User import route_user


MODULES = (
    ( route_index, '/' ),
    ( route_static, '/static' ),
    ( route_user, '/user' )
)


def setting_modules(app, modules):
    """ 注册Blueprint模块 """
    for module, url_prefix in modules:
        app.register_blueprint(module, url_prefix=url_prefix)

setting_modules(app, MODULES)


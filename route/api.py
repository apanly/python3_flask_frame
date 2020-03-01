# -*- coding: utf-8 -*-
'''
专门为wapi程序准备的初始化入口
'''

'''
统一拦截处理和统一错误处理
'''
from api.interceptors.Auth import  *
from api.interceptors.ErrorHandler import  *


'''
蓝图功能，对所有的url进行蓝图功能配置
'''
from api.controllers.index import route_index


MODULES = (
    ( route_index, '/' ),
)


def setting_modules(app, modules):
    """ 注册Blueprint模块 """
    for module, url_prefix in modules:
        app.register_blueprint(module, url_prefix =  url_prefix)

setting_modules(app, MODULES)


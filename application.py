# -*- coding: utf-8 -*-
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import sys,os

class Application(Flask):
    def __init__(self, import_name,template_folder = None,static_folder = None,root_path = None):
        super(Application, self).__init__(import_name,template_folder = template_folder,static_folder = static_folder,root_path = root_path)
        self.config.from_pyfile('config/base_setting.py')
        if "ops_config" in os.environ:
            self.config.from_pyfile( 'config/%s_setting.py'%( os.environ['ops_config'].strip() ) )

        db.init_app(self)

    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        if endpoint is None:
            endpoint = rule

        super(Application, self).add_url_rule(   rule,   endpoint=endpoint, view_func=view_func,  **options )

db = SQLAlchemy()
app = Application( __name__ ,template_folder = None ,static_folder = None,root_path = os.getcwd() )
manager = Manager( app )

'''
函数模板
'''
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildWWWUrl, 'buildUrl')


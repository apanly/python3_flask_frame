# -*- coding: utf-8 -*-
from application import  app
'''
python manage.py runjob -m folder/test  -a list | parse
'''


class JobTask():
    def __init__(self):
        pass

    def run(self, params):
        act = params['act']
        #先获取在解析
        if act == "list":
            app.logger.info( "this is list " )
        elif act == "parse":
            app.logger.info("this is parse ")


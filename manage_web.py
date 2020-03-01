# -*- coding: utf-8 -*-
from application import app,manager
from flask_script import Server
from route.www import *
import os
##web server
manager.add_command('runserver', Server(host='0.0.0.0', port=app.config.get('SERVER_PORT'), use_debugger=True))

##设置模板路径
app.template_folder = os.getcwd() + "/web/templates/"

def main():
    manager.run()

if __name__ == '__main__':
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        app.logger.info( e )
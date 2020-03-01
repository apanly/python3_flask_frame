# -*- coding: utf-8 -*-
from application import app, manager
from flask_script import Server
from route.api import *

##api server
manager.add_command('runserver', Server(host='0.0.0.0', port=app.config.get('API_SERVER_PORT'), use_debugger=True))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        app.logger.info(e)

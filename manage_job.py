# -*- coding: utf-8 -*-
from application import app,manager

from jobs.launcher import runJob,jobList

#job entrance
manager.add_command('runjob', runJob() )
manager.add_command('joblist', jobList() )

def main():

    manager.run()

if __name__ == '__main__':
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        app.logger.info( e )
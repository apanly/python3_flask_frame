# -*- coding: utf-8 -*-
from application import app
from common.libs.DateUtil import getCurrentTime
import os

class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildWWWUrl( path ):
        config_domain = app.config['DOMAIN']
        return "%s%s"%( config_domain['www'],path )

    @staticmethod
    def buildStaticUrl(path):
        ver = UrlManager.getReleaseVersion()
        path =  "/static" + path + "?ver=" + ver
        return UrlManager.buildWWWUrl( path )


    @staticmethod
    def getReleaseVersion():
        ver = "%s" % (getCurrentTime("%Y%m%d%H%M%S%f"))
        release_path = app.config.get('RELEASE_PATH')
        if release_path and os.path.exists( release_path ):
            with open( release_path , 'r') as f:
                ver = f.readline()

        return ver
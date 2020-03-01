# -*- coding: utf-8 -*-

from application import app
from flask import Flask,request,redirect,g,make_response

from common.models.User import ( User )
import common.libs.Helper
from common.libs.UrlManager import ( UrlManager )
import re

@app.before_request
def before_request():
    return


@app.after_request
def after_request( response ):
    return response

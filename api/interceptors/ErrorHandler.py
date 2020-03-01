# -*- coding: utf-8 -*-

from application import app
from common.libs.Helper import ops_renderJSON

@app.errorhandler(404) #捕获应用的异常
def error_404(e):
    return ops_renderJSON( 404,"很抱歉！,您访问的页面不存在 ~~" )


@app.errorhandler(405) #捕获应用的异常
def error_404(e):
    return ops_renderJSON( 405,"所有请求必须POST请求" )

@app.errorhandler(500) #捕获应用的异常
def error_500(e):
    return ops_renderJSON( 500,"服务器错误 ~~" )

@app.errorhandler(502) #捕获应用的异常
def error_502(e):
    return ops_renderJSON(500, "服务器错误 ~~")



# -*- coding: utf-8 -*-
from application import app
from flask import Blueprint,jsonify,make_response,request,redirect,g
from common.libs.Helper import ops_renderView,userAuthToken
import json,smtplib
from  common.models.User import ( User )
from common.libs.UrlManager import ( UrlManager )
import common.libs.Constant

route_user = Blueprint('user_page', __name__)

@route_user.route("/login",methods = [ "GET","POST" ])
def Login( ):
    if request.method == "GET":

        if g.current_user:
            return  redirect( UrlManager.buildWWWUrl("/") )
        return ops_renderView("user/login.html")

    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values
    email = req['email'] if 'email' in req else ''
    pwd = req['pwd'] if 'pwd' in req else ''

    if  email is None or len( email ) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的邮箱~~"
        return jsonify( resp )

    if  pwd is None or len( pwd ) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的邮箱密码~~"
        return jsonify(resp)

    user_info = User.query.filter_by( email = email ).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "你好，未注册的邮箱，请找系统管理员先注册用户~~"
        return jsonify(resp)

    try:
        at_idx = email.index( "@" )
        smtpObj = smtplib.SMTP_SSL( "smtp." + email[ (at_idx +1): ],465 )
        smtpObj.set_debuglevel(1)
        smtpObj.login(email, pwd)
        smtpObj.close()
    except Exception:
        resp['code'] = -1
        resp['msg'] = "登录失败,请核对邮箱和密码是否对应~~"
        return jsonify(resp)

    next_url = UrlManager.buildWWWUrl( "/" )

    response = make_response(json.dumps({ 'code': 200, 'msg': '登录成功~~','data':{ "next_url":next_url } }))
    response.set_cookie( common.libs.Constant.AUTH_COOKIE_NAME, '%s#%s' % ( userAuthToken(user_info), user_info.id),  60 * 60 * 24 * 120)  # 保存120天
    return response

@route_user.route("/logout")
def LogOut(  ):
    response = make_response( redirect( UrlManager.buildWWWUrl( "/user/login" ) ) )
    response.delete_cookie( common.libs.Constant.AUTH_COOKIE_NAME )
    return response


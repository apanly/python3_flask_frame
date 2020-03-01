# -*- coding: utf-8 -*-
import hashlib
from flask import render_template,g,jsonify

def ops_renderView(  template, context = {} ):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template( template , **context)


def ops_renderJSON( code = 200,msg = "操作成功~~",data = {},flag = True ):
    if flag == False:
        code = 0

    resp = {'code': code, 'msg': msg, 'data': data }
    return jsonify( resp )


'''
写入文件
'''

def writeFile( file_path = None,data = None ):
    with open( file_path , 'wb') as f:
        f.write( data )


'''
用户信息加密
可以把多个字段进行加密，还可以把状态放到里面，这样状态变了就会立即退出
'''
def userAuthToken(user_info):
    m = hashlib.md5()
    str = "%s-%s-%s-%s" % (user_info.id, user_info.email, user_info.salt,user_info.name)
    m.update(str.encode("utf-8"))
    return m.hexdigest()





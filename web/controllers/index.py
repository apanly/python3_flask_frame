# -*- coding: utf-8 -*-
from flask import Blueprint
from common.libs.Helper import ops_renderView

route_index = Blueprint('index_page', __name__)

@route_index.route("/")
def index():
    return ops_renderView( "index/index.html"  )
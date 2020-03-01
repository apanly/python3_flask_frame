# -*- coding=utf-8 -*-
from application import db

class User( db.Model ):
    __tablename__ = 'user'
    id = db.Column( db.BigInteger, primary_key=True)
    name = db.Column(db.String(20), nullable=False, server_default=db.text("''"))
    email = db.Column( db.String(50),unique=True, nullable=False,server_default = db.text("''") )
    salt = db.Column( db.String(64),unique=True, nullable=False,server_default = db.text("''") )
    update_time = db.Column( db.DateTime, nullable=False,server_default = db.text("0000-00-00 00:00:00") )
    create_time = db.Column( db.DateTime, nullable=False,server_default = db.text("0000-00-00 00:00:00") )

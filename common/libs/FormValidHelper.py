# -*- coding: utf-8 -*-
from application import  app
import re

def checkDate( str_date = '',fmt = r'^\d{4}-\d{2}-\d{2}$' ):
    return (  str_date is not None and len( str_date ) > 0  and  re.match( fmt,str_date ) != None )

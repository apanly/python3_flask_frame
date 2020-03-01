# -*- coding: utf-8 -*-
from __future__ import division
import datetime

def getCurrentTime(fmt="%Y-%m-%d %H:%M:%S", date=None ):
    return getFormatDate( date = date,format = fmt)

'''
获取格式化的时间
'''
def getFormatDate( date = None ,format = "%Y-%m-%d %H:%M:%S" ):
    if date is None:
        date = datetime.datetime.now()

    return date.strftime( format )

def getDateBefore(day=1 , date  = None ):
    if date is None:
        date = datetime.date.today()
    return date - datetime.timedelta( days=day )

def getDateAfter( day=1,date  = None):
    if date is None:
        date = datetime.date.today()
    return date + datetime.timedelta(days=day)

def calAge( born ):
    today = datetime.date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, day=born.day - 1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

# 计算生肖
def chineseZodiac(year):
    return  year % 12

#计算星座
def zodiac(month, day):
  d = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
  a_list = list( filter( lambda y: y <= ( month ,day ), d ) )
  return len( a_list ) % 12


def getCurrentWeekRange():
    now = datetime.datetime.now()
    this_week_start = now - datetime.timedelta( days = now.weekday() )
    this_week_end = now + datetime.timedelta( days = 6 - now.weekday() )
    return [ this_week_start, this_week_end]

def getWeekRange( date = None,fmt = None ):
    now = datetime.datetime.now()
    if date is not None:
        now = date
    week_start = now - datetime.timedelta( days = now.weekday() )
    week_end = now + datetime.timedelta( days = 6 - now.weekday())
    if fmt is not None:
        week_start = getCurrentTime( fmt = fmt,date = week_start )
        week_end = getCurrentTime( fmt = fmt,date = week_end )
    return [week_start, week_end]


def getMonthRange( date = None,fmt = None ):
    now = datetime.datetime.now()
    if date is not None:
        now = date
    month_start = datetime.datetime(now.year, now.month, 1)
    month_end = month_start + datetime.timedelta( days = 30 )  - datetime.timedelta( days = 1 )
    if fmt is not None:
        month_start =  getCurrentTime( fmt = fmt,date = month_start )
        month_end = getCurrentTime( fmt = fmt,date = month_end )
    return [ month_start,month_end ]

def str2Date( date = None,fmt = None,is_datetime = True ):
    ret = datetime.datetime.strptime( str( date ) , fmt )
    if not is_datetime:
        ret = ret.date()
    return ret


def diffDays(d1,d2):
    return ( d1 - d2 ).days


def weekNumOfYear( date = None ):
    now = datetime.datetime.now()
    if date is not None:
        now = date
    return now.isocalendar()[1]

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= crawler
@author= wubingyu
@create_time= 2017/12/23 上午9:16
"""
import urllib2
import urllib

# response = urllib2.urlopen("http://www.douban.com")
# print response.read()
#
# #post
# values = {"username": "flybetter@163.com", "password": "xxx"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login"
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print response.read()


# get
values = {}
values["username"] = "flybetter@163.com"
values["password"] = "xxx"
url = "http://mp.gamecomb.com/s.do"
geturl = url + '?' + urllib.urlencode(values)
print geturl
response = urllib2.urlopen(geturl)
print response.read()

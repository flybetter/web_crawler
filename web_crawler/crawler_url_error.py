#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= URLError
@author= wubingyu
@create_time= 2017/12/23 上午11:36
"""
import urllib2

req = urllib2.Request("http://www.xxx.com")
try:
    resp = urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e, "reason"):
        print e.reason
else:
    print "ok"

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= error_code
@author= wubingyu
@create_time= 2017/12/26 下午4:40
"""
from pyquery import PyQuery as pq
import HTMLParser

pd = pq(url='http://www.baidu.com')
h = HTMLParser.HTMLParser()
print h.unescape(pd)
print pd

print h.unescape('&#231;&#153;&#190;')

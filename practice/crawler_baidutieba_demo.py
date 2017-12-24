#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= crawler_baidutieba_demo
@author= wubingyu
@create_time= 2017/12/24 下午9:05
"""
import urllib2
import re

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
url = 'https://tieba.baidu.com/p/3138733512?see_lz=1&pn=1'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()


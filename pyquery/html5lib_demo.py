#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= html5lib_demo
@author= wubingyu
@create_time= 2017/12/25 下午11:46
"""
import html5lib
import requests
import urllib2
import lxml

re=requests.post("https://www.baidu.com")
print re.text


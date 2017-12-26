#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= html5lib_demo
@author= wubingyu
@create_time= 2017/12/25 下午11:46
"""
from lxml import etree
import requests
from lxml.html import fromstring,tostring

page = 1
url = 'http://www.jikexueyuan.com/course/?pageNum=' + str(page)
html = requests.get(url)

print html.text


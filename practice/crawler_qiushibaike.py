#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= crawler_qiushibaike
@author= wubingyu
@create_time= 2017/12/24 上午10:38
"""
import re
import urllib2

# qsbaikeUrl = "https://www.douban.com"
page = 1
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
qsbaikeUrl = "https://www.qiushibaike.com/hot/page" + str(page)
req = urllib2.Request(qsbaikeUrl, headers=headers)
resp = urllib2.urlopen(req)
content = resp.read().decode('utf-8')
pattern = re.compile("<span>(\s*)(.*?)(\s*)</span>")
result = re.finditer(pattern, content)
for k, data in enumerate(result):
    print "--------line", k
    print re.sub(r"<.*?>", "", data.group(2))
    # print data.groups()

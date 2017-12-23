#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= crawler_urllib
@author= wubingyu
@create_time= 2017/12/23 上午10:31
"""
import urllib
import urllib2

values = {"username": "flybetter@163.com", "password": "1234"}
agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
url = "http://www.douban.com"
headers = {"User-Agent": agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
print response.read()

# 2.change the proxy
proxy_handler = urllib2.ProxyHandler({"http": "http://www.douban.com:8080"})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)

proxy = urllib2.ProxyHandler({"http": "http://www.douban.com"})
open_builder = urllib2.build_opener(proxy)
urllib2.install_opener(open_builder)

# 3 timeout settings
response = urllib2.urlopen("http://www.douban.com", timeout=20)
print response.read()

# 4 HTTP's request mode settings
url = "http://www.douban.com"
request = urllib2.Request(url)
request.get_method = "put"
response = urllib2.urlopen(request)
print response

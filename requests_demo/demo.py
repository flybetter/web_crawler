#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= demo
@author= wubingyu
@create_time= 2017/12/25 下午3:42
"""
import requests
import json

# get
r = requests.get('http://cuiqingcai.com')
baseUrl = 'http://httpbin.org/post'
print type(r)
print r.status_code
print r.encoding
print r.cookies

payload = {"key1": "value1", "key2": "value2"}
r = requests.get("http://www.baidu.com", payload)
print r.url

r = requests.get("https://github.com/timeline.json", stream=True)
print r.raw
print r.raw.read()

headers = {"content-type": "application/json"}
r = requests.get("http://www.baidu.com", payload, headers=headers)
print r.url

# post
r = requests.post(baseUrl, data=payload)
print r.text

r = requests.post(baseUrl, data=json.dumps(payload))
print r.text

files = {"files": open('__init__.py', 'rb')}
r = requests.post(baseUrl, files=files)
print r.text

# 不需要存放内存,直接通过流的方式上传

with open("__init__.py", "rb") as f:
    r = requests.post(baseUrl, data=f)
    print r.text

# cookie
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print r.text

# 超时配置
# r = requests.get(baseUrl, timeout=0.001)
# print r.text

s = requests.session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print r.text

# SSL证书验证
r = requests.get("https://kyfw.12306.cn/otn/", verify=True)
print r.text

# 代理
proxies = {
    "https": "http://41.118.132.69:4433"
}

r = requests.post("http://httpbin.org/post", proxies=proxies)
print r.text

r = requests.post("http://www.baidu.com")
print r.text

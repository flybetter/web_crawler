#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= crwaler_cookie
@author= wubingyu
@create_time= 2017/12/23 下午10:00
"""
import urllib2
import cookielib
import urllib

# 1 Opener .urlopen

# 2 Cookielib
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
resp = opener.open("https://www.baidu.com")
for item in cookie:
    print item.name
    print item.value

filename = "cookie.txt"
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
resp = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)

cookie = cookielib.MozillaCookieJar
cookie.load(filename='cookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
opener.open("http://www.douban.com")

filename2 = "cookie.txt"
cookie = cookielib.MozillaCookieJar(filename2)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({'stuid': '201200131012', 'pwd': '23342321'})
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
resp = opener.open(loginUrl, postdata)
cookie.save(ignore_discard=True, ignore_expires=True)

gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
gradeResp = opener.open(gradeUrl)
print gradeResp



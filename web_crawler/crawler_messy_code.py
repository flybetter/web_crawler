#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= crawler_messy_code
@author= wubingyu
@create_time= 2017/12/23 上午9:32
"""
import urllib2
import sys

type = sys.getfilesystemencoding()


def main():
    url = "http://www.douban.com"
    # 浏览器头
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(url=url, headers=headers)
    data = urllib2.urlopen(req).read()
    print data.decode("UTF-8").encode(type)
    return 0


if __name__ == '__main__':
    main()

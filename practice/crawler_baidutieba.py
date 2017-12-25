#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= crawler_baidutieba
@author= wubingyu
@create_time= 2017/12/24 下午9:51
"""
import urllib2
import re
import os


class BDTB:
    def __init__(self, baseUrl, seeLz):
        self.baskUrl = baseUrl
        self.seeLz = '?see_lz=' + str(seeLz)

    def getPage(self, pageNum):
        try:
            url = self.baskUrl + self.seeLz + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u'连接百度贴吧失败,错误原因:', e.reason
                return None

                # <h3 class="core_title_txt pull-left text-overflow  "
                # title="纯原创我心中的NBA2014-2015赛季现役50大" style="width: 396px">
                # 纯原创我心中的NBA2014-2015赛季现役50大</h3>

    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            print result.group(1)
            return result.group()
        else:
            return None

            # <li class="l_reply_num" style="margin-left:8px"><span class="red" style="margin-right:3px">141</span>
            # 回复贴，共<span class="red">5</span>页</li>

    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?><span.*?>.*?</span>.*?'
                             '<span class="red">(.*?)</span>.*?</li>', re.S)
        result = re.search(pattern, page)
        if result:
            print result.group(1)
            return result.group()
        else:
            return None

    # <div id="post_content_53073988951" class="d_post_content j_d_post_content ">

    def getContent(self):
        page = self.getPage(1)
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        result = re.finditer(pattern, page)
        result_content = ""
        if result:
            for data in result:
                result_content += re.sub('<.*?>|\s', '', data.group(1))+os.linesep
                print re.sub('<.*?>|\s', '', data.group(1))
        else:
            result_content += "None"
        return result_content


#baseURL = 'https://tieba.baidu.com/p/3138733512'
baseURL = 'https://zhuanlan.zhihu.com/p/24012671'
#baseURL = 'http://tieba.baidu.com/p/5431205655'
badt = BDTB(baseURL, 1)
print badt.getPage(1)
# badt.getTitle()
# badt.getPageNum()
#content = badt.getContent()

# with open("baidutieba.txt", "w+")as f:
#     f.write(content)

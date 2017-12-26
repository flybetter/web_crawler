#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= pyquery_demo
@author= wubingyu
@create_time= 2017/12/26 上午10:43
"""
from pyquery import PyQuery as pq
from lxml import etree
import HTMLParserx
import urllib

d = pq("<html></html>")
print d
d = pq(etree.fromstring("<html></html>"))
print d

d = pq(url='http://www.douban.com/')
print d

print d("#form")

p = d("#form")
print p.html()

p.html("you know <a href='http://python.org/'>Python</a>rocks")
print p.html()

print p.text()

p = pq('<p id="hello" class="hello"></p>')
print p.attr('id')

p.attr('id', 'plop')
print p
print type(p)

p.attr('class', '111')
print p
print type(p)

p.toggle_class("111 wubi")
print p

p.remove_class("wubi")
print p

p.add_class("biwu")
print p

p.css("font-szie", "15px")
print p

# manipulating

d = pq('<p class="hello" id="hello">you know python rocks</p><p class="hello" id="hello">you know python rocks</p>')
d('p:first').append('check out')
print d

p = d('p')
p.prepend('check out <a href="https://"></>')
print p

d = pq('<html><body><div id="test"><a href="http://python.org">python</div></body></html>')
p.appendTo(d("#test"))
print d("#test").html()

#Traversing
d = pq('<p id="hello" class="hello"><a/></p><p id="test"><a/></p>')
print d('p').filter('.hello').html()
print d('p').find('a').end()
print d.show()

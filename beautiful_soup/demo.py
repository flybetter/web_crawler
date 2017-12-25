#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= demo
@author= wubingyu
@create_time= 2017/12/25 下午4:51
"""
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)
print soup.prettify()

# 四大对象种类 Tag NavigableString BeautifulSoup Comment
#tag
print soup.title
print soup.head
print soup.a
print type(soup.a)
#对于tag,它有两个重要的属性，是name和attrs,下面我们分别来感受一下
print soup.name
print soup.head.name
print soup.p.attrs
print soup.p['class']
print soup.p.get('class')
soup.p['class']="newClass"
print soup.p

#NavigableString
print soup.p.string

#BeautifulSoup 是一个特殊的tag
print soup.name

#Comment 是一种特殊类型的NavigableString对象,其实输出的内容
#自动对注释的内容去掉了
print soup.a
print soup.a.string
print type(soup.a)

#遍历文档树
print soup.head.contents



#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= demo
@author= wubingyu
@create_time= 2017/12/27 上午11:06
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('http://www.python.org')
print driver.title
assert "Welcome to Python.org" in driver.title
elem = driver.find_element_by_id("id-search-field")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print driver.page_source

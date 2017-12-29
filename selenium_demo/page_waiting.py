#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= page_waiting
@author= wubingyu
@create_time= 2017/12/29 上午11:12
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(By.ID, "myDynamicElement")
    )
finally:
    driver.quit()

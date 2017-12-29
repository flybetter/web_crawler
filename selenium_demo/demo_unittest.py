#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= demo_unittest
@author= wubingyu
@create_time= 2017/12/29 上午10:38
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Welcome to Python.org", driver.title)
        elem = driver.find_element_by_id("id-search-field")
        elem.send_keys("py")
        elem.send_keys(Keys.RETURN)
        print driver.page_source
        assert "No results founds" not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

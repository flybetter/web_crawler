#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= thread_demo
@author= wubingyu
@create_time= 2018/1/4 上午11:04
"""
import time
import thread


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count + 1
        print "%s:%s" % (threadName, time.ctime(time.time()))


try:
    thread.start_new_thread(print_time, ("thread-1", 2,))
    thread.start_new_thread(print_time, ("thread-2", 4,))
except:
    print "Error:unable to create the thread"

while 1:
    pass

print "Main Finished"

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= process_demo
@author= wubingyu
@create_time= 2018/1/4 下午1:30
"""
import multiprocessing
import time


def process(num):
    time.sleep(num)
    print "process:", num


if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()

    print "CPU number" + str(multiprocessing.cpu_count())
    for i in multiprocessing.active_children():
        print ("Child process name" + p.name + 'id:' + str(p.pid))

print ("Process Ended")

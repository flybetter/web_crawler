#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= web_crawler
@file= threads_model_demo
@author= wubingyu
@create_time= 2018/1/4 上午11:11
"""
import threading
import thread
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print "%s:%s" % (threadName, time.ctime(time.time()))
        counter -= 1


thread1 = MyThread(1, "thread-1", 1)
thread2 = MyThread(2, "thread-2", 2)

thread1.start()
thread2.start()

print "Exiting Main Thread"

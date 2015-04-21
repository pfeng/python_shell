# !/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue
import threading
import urllib2
import time

hosts = ["http://www.baidu.com", "http://www.163.com", "http://www.weibo.com",
         "http://www.sina.com", "http://www.oschina.net"]

queue = Queue.Queue()


class ThreadUrl(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            host = self.queue.get()
            # 设置头信息
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = {'Connection': 'keep-alive', 'User-Agent': user_agent}
            req = urllib2.Request(host, None, headers=headers)
            res = urllib2.urlopen(req)
            print res.read(1024)+"\n-----------------"
            self.queue.task_done()


def start():
    for i in range(len(hosts)):
        t = ThreadUrl(queue)
        t.setDaemon(True)
        t.start()

    for host in hosts:
        queue.put(host)
    queue.join()


if __name__ == '__main__':
    start()

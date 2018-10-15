# -*- coding: utf-8 -*-

import threading
import time


class TestThread(threading.Thread):

    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):  # 线程在start后会直接运行run函数
        func(self.name, self.delay)


def func(name, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print name, time.ctime(time.time()), count


thread1 = TestThread("Thread-1", 3)
thread2 = TestThread("Thread-2", 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
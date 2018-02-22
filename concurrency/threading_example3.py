# 让要执行的线程继承自Thread
# 执行start方法调用的是线程类的run方法
# 通过multiprocessing模块在一个单独的进程中执行代码

from threading import Thread
from multiprocessing import Process
import time

class CountDownThread(Thread):
    def __init__(self,n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print ('T-minus ',self.n)
            self.n -= 1
            time.sleep(1)

c = CountDownThread(5)
p = Process(target=c.run)
p.start()
# python threading的简单例子
# 把线程放入类中/把类的方法传给Thread


import time
from threading import Thread


class CountDownTask:
    def __init__(self):
        self._running=True

    def tearDown(self):
        self._running=False

    def run(self,n):
        while self._running == True and n>0:
            print ('T-minus ', n)
            n -= 1
            time.sleep(1)

c = CountDownTask()
t1 = Thread(target=c.run, args=(10,))
t1.start()
time.sleep(5)
c.tearDown()
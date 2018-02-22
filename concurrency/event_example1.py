# Event对象实现线程的同步
# Event对象为真时，唤醒所有等待的对象
# Event对象为假时，所有等待的对象阻塞
# Event对象创建时，默认为假
# Event对象最好单次使用，也就是当设置了Event对象为真时，应该丢弃它，不建议clear后再继续使用
# Event对象会唤醒所有的线程，如果只唤醒单个线程，使用信号量或者Condition对象

import time
from threading import Thread, Event


def countdown(n, start_event):
    start_event.wait()
    print('start count')
    while n>0:
        print('T-minus ',n)
        n -= 1
        time.sleep(1)


start_event = Event()
t1 = Thread(target=countdown, args=(5,start_event,))
t1.start()
print('main thread')
time.sleep(5)
print('set event is True')
start_event.set()


# Event对象会唤醒所有的线程，如果只唤醒单个线程，使用信号量或者Condition对象


from threading import Thread, Semaphore
import time


def worker(n,sema):
    sema.acquire()
    print('this is worker ',n)
    time.sleep(1)
    sema.release()


sema = Semaphore(5)
for i in range(10):
    t = Thread(target=worker, args=(i,sema))
    t.start()
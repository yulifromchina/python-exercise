# python threading的简单例子
# threading.Thread用于创建线程
# start()方法用于运行线程
# join()方法用于同步阻塞，等待线程结束
# daemon=True用于设置守护进程，守护进程是后台进程，随主线程结束而销毁

import time
from threading import Thread

def countDown(n):
    while n>0:
        print('T-minus ',n)
        n -= 1
        time.sleep(1)

t1 = Thread(target=countDown, args=(5,))
t1.start()
t1.join()
t2 = Thread(target=countDown, args=(5,),daemon=True)
t2.start()
print('all main thread')
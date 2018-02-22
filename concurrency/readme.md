未整理完。。。。。。

### python进程的模块：

**thread:** python3中以及遗弃

**threading**，常用如下：

```
t1 = threading.Thread(target=xxx,args=(xxx,))

t1.start()/t1.join()

t1.daemon=True
```

### 线程间通信：

**1.Event()对象：**

```
event = Event() # 信号默认为False

event.set()  # 信号设置为True

event.wait()  #等待信号为True，否则阻塞等待
```

**2.Condition对象（条件变量）**

**3.Semaphore对象（信号量）：**

```
sema = Semaphore(n)

sema.acquire()

sema.release()
```

**4.Queue对象(队列)**：

```
from queue import Queue

q = Queue()

q.put(xxx)/q.get()
```



### 同步原语：

**1.Lock()对象**:

```
lock=threading.Lock()

lock.acquire()/lock.release()

with lock:xxx
```

**2.RLock对象（可重入锁）**


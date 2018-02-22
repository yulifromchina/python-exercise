# 多线程环境，给临界区加锁以避免竞争条件
# Lock对象和with一起使用，会在with使用前加锁/with使用后自动释放锁

import threading


class SharedCounter:
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def increment(self, delta=1):
        with self._value_lock:
            self._value += delta
        """
        相当于：
        self._value_lock.acquire()
        self._value += delta
        self._value_lock.release()
        """

    def decrement(self, delta=1):
        with self._value_lock:
            self._value -= delta
        """
        相当于：
        self._value_lock.acquire()
        self._value -= delta
        self._value_lock.release()
        """



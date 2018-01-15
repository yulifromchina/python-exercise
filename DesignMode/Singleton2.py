# -*- coding:utf-8 -*-
#用装饰器实现单例模式

class Singleton(object):
    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
        return self._instance

@Singleton
class A:
    def __init__(self):
        pass

    def display(self):
        return id(self)


if __name__ == '__main__':
    s1 = A.Instance()
    s2 = A.Instance()
    print(s1, s1.display())
    print(s2, s2.display())
    print(s1 is s2)
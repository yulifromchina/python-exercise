# -*- coding:utf-8 -*-
#用抽象基类实现策略模式

import abc


class AbsShow(object):
    """
    抽象显示对象
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def show(self):
        pass


class AdminShow(AbsShow):
    """
    管理员的显示操作
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def show(self):
        return 'show with admin'


class UserShow(AbsShow):
    """
    普通用户的显示操作
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def show(self):
        return 'show with usr'


class Question(object):
    def __init__(self, show_obj):
        self.show_obj = show_obj

    def show(self):
        return self.show_obj().show()


if __name__ == '__main__':
    q = Question(show_obj = AdminShow)
    print(q.show())
    q.show_obj = UserShow
    print(q.show())



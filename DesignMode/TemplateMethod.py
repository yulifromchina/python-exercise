# -*- coding:utf-8 -*-
# 模板方法模式

import abc

class Fishing(object):
    """
    钓鱼模板基类
    """
    __metaclass__ = abc.ABCMeta

    def fishing(self):
        self.prepare_bait()
        self.go_to_riverbank()
        self.find_location()
        print('start fishing.')

    @abc.abstractmethod
    def prepare_bait(self):
        pass

    @abc.abstractmethod
    def go_to_riverbank(self):
        pass

    @abc.abstractmethod
    def find_location(self):
        pass


class JohnFishing(Fishing):
    """
    John想去钓鱼，他需要实现钓鱼的三步骤
    """

    def prepare_bait(self):
        """
        从淘宝买鱼饵
        """
        print('John: buy bait from taobao')

    def go_to_riverbank(self):
        """
        开车去钓鱼
        """
        print('John : to river by driving')

    def find_location(self):
        """
        在岛上选择钓鱼点
        """
        print('John: select location on the island.')


class SimonFishing(Fishing):
    """
    Simon也想去钓鱼，它也必须实现钓鱼的三步骤
    """

    def prepare_bait(self):
        """
        从京东购买鱼饵
        """
        print('Simon: buy bait from JD')

    def go_to_riverbank(self):
        """
        骑自行车去钓鱼
        """
        print('Simon: to river by biking')

    def find_location(self):
        """
        在河边选择钓鱼
        """
        print('Simon: select location on the riverbank')


if __name__ == '__main__':
    f = JohnFishing()
    f.fishing()
    f1 =  SimonFishing()
    f1.fishing()
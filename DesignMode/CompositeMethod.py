# -*- coding:utf-8 -*-
import abc

class Worker(object):
    """
    员工抽象类
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def work(self):
        pass


class Employee(Worker):
    """
    员工类
    """
    __metaclass__ = abc.ABCMeta

    def work(self):
        print('Employee %s start to work' % self.name)


class Leader(Worker):
    """
    领导类
    """

    def __init__(self, name):
        self.members = []
        super(Leader, self).__init__(name)

    def add_member(self, employee):
        if employee not in self.members:
            self.members.append(employee)

    def remove_member(self, employee):
        if employee in self.members:
            self.members.remove(employee)

    def work(self):
        print('Leader %s start work' % self.name)
        for employee in self.members:
            employee.work()



if __name__=='__main__':
    employee1 = Employee('employee1')
    employee2 = Employee('employee2')
    leader1 = Leader('leader1')
    leader1.add_member(employee1)
    leader1.add_member(employee2)
    leader1.work()
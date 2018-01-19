# -*- coding:utf-8 -*-
import abc

class Subject(object):
    """
    被观察对象的基类
    """
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """
        注册观察者
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """
        注销一个观察者
        """
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        """
        通知所有观察者
        """
        for observer in self._observers:
            observer.update(self)#注意传递的是自身


class Course(Subject):
    """
    课程对象，被观察的对象
    """
    def __init__(self):
        super(Course, self).__init__()
        self._message = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message
        self.notify()


class Observer(object):
    """
    观察者抽象类
    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, subject):
        pass


class UserOberser(Observer):
    """
    用户观察者
    """

    def update(self, subject):
        print ('UserObserver  {}'.format(subject.message))



class OrgOberser(Observer):
    """
    机构观察者
    """

    def update(self, subject):
        print ('OrgObserver {}'.format(subject.message))



if __name__ == '__main__':
    user = UserOberser()
    org = OrgOberser()

    course = Course()
    course.attach(user)
    course.attach(org)

    course.message = 'two observer'

    course.detach(user)
    course.message = 'one observer'
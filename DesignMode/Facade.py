# -*- coding:utf-8 -*-

class User(object):
    """
    用户类
    """
    def is_login(self):
        return True

    def has_privilege(self, privilege):
        return True


class Course(object):
    """
    课程类
    """
    def can_be_learned(self):
        return True


class Lab(object):
    """
    实验类
    """
    def can_be_started(self):
        return True



class Client(object):
    """
    客户类
    """
    def __init__(self, usr, course, lab):
        self.user = usr
        self.course = course
        self.lab = lab

    def start_lab(self):
        if self.user.is_login() and self.course.can_be_learned() and self.lab.can_be_started():
            print ('start lab')
        else:
            print ('cannot start lab')



class Facade(object):
    """
    新的lab类，应用了面向对象模式
    """
    def __init__(self, user, course, lab):
        self.user = user
        self.course = course
        self.lab = lab

    def can_be_started(self):
        if self.user.is_login() and self.course.can_be_learned() and self.lab.can_be_started():
            return True
        else:
            return False


class NewClient(object):
    """
    新的客户类，使用了外观模式
    """
    def __init__(self, facade_lab):
        self.lab = facade_lab

    def start_lab(self):
        """
        开始实验，只需要判断FacadeLab是否可以开始
        """
        if self.lab.can_be_started():
            print('lab start')
        else:
            print('lab cannot start')



if __name__=='__main__':
    user = User()
    course = Course()
    lab = Lab()
    client = Client(user, course, lab)
    client.start_lab()

    print('Use Facade Patterns:')
    facade_lab = Facade(user, course, lab)
    facade_client = NewClient(facade_lab)
    facade_client.start_lab()
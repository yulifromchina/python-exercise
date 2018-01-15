# -*- coding:utf-8 -*-
#用抽象基类实现工厂模式

import random
import abc

class BasicCourse(object):
    """
    基础课程
    """
    def get_lab(self):
        return 'basic course'


class ProjectCourse(object):
    """
    项目课程
    """
    def get_lab(self):
        return 'project course'


class Factory(object):
    """
    抽象工厂类
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_course(self):
        pass


class BasicCourseFactory(Factory):
    """
    基础课程工厂类
    """
    def create_course(self):
        return BasicCourse()


class ProjectCourseFactory(Factory):
    """
    项目课程工厂类
    """
    def create_course(self):
        return ProjectCourse()


def get_factory():
    """
    随机获取一个工厂类
    :return:
    """
    return random.choice([BasicCourseFactory, ProjectCourseFactory])()


if __name__ == '__main__':
    factory = get_factory()
    course = factory.create_course()
    print(course.get_lab())
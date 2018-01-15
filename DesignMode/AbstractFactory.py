# -*- coding:utf-8 -*-
#用抽象基类实现抽象工厂模式

import random
import abc

#两种类型的课程
class BasicCourse(object):
    def get_lab(self):
        return 'basic course'


class ProjectCourse(object):
    def get_lab(self):
        return 'project course'


#两种类型的虚拟机
class LinuxVim(object):
    def start(self):
        return 'Linux vim is running'


class MacVim(object):
    def start(self):
        return 'Mac vim is running'


class Factory(object):
    """
    抽象工厂类，含有创建虚拟机和课程的抽象方法
    """
    __mateclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_course(self):
        pass

    @abc.abstractmethod
    def create_vm(self):
        pass


class BasicCourseFactory(object):
    """
    基础课程工厂类
    """
    def create_course(self):
        return BasicCourse()

    def create_vm(self):
        return LinuxVim()


class ProjectCourseFactory(object):
    """
    项目工厂类
    """
    def create_course(self):
        return ProjectCourse()

    def create_vm(self):
        return MacVim()


def get_factory():
    return random.choice([BasicCourseFactory, ProjectCourseFactory])()


if __name__ == '__main__':
    factory = get_factory()
    course = factory.create_course()
    vim = factory.create_vm()
    print(course.get_lab())
    print(vim.start())
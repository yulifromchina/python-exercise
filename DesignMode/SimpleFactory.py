# -*- coding:utf-8 -*-
#用静态方法实现简单工厂模式

import random

class BasicCourse(object):
    def get_lab(self):
        return 'basic_course:labs'


class ProjectCourse(object):
    def get_lab(self):
        return 'project_course:labs'


class SimpleCourseFactory(object):

    @staticmethod
    def create_course(type):
        if type == 'bc':
            return BasicCourse()
        elif type == 'pc':
            return ProjectCourse()


if __name__=='__main__':
    t = random.choice(['bc','pc'])
    course = SimpleCourseFactory.create_course(t)
    print(course.get_lab())
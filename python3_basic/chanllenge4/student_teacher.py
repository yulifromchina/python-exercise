#!/usr/bin/env python3
#coding=utf-8

import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self, grade):
        c = Counter(grade)
        pass_num = c['A']+c['B']+c['C']
        fail_num = c['D']
        print("Pass : {}, Fail : {}".format(pass_num, fail_num))
        

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self, grade):
        c = Counter(grade)
        print("A: {}, B: {}, C:{}, D:{}".format(c['A'], c['B'],c['C'],c['D']))



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Invalid Paramter.")
       
    if sys.argv[1]=="student":
        student = Student("temp","temp","temp")
        student.get_grade(sys.argv[2])

    if sys.argv[1] == "teacher":
        teacher= Teacher("temp","temp")
        teacher.get_grade(sys.argv[2])

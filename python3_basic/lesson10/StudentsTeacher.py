#!/usr/bin/env python3

class Person(object):
	"""
	return Person object
	"""
	
	def __init__(self, name):
		self.name = name

	def get_details(self):
		return self.name


class Student(Person):
	"""
	return Students object
	"""
		
	def __init__(self, name, branch, year):
		Person.__init__(self, name)
		self.branch = branch
		self.year = year

	def get_details(self):
		return "{} student study {} and is in {} year.".format(self.name, self.branch, self.year)
	

class Teacher(Person):
	"""
	return Teacher object
	"""
	def __init__(self, name, papers):
		Person.__init__(self, name)
		self.papers = papers

	def get_details(self):
		return "{} teaches {}.".format(self.name, self.papers)


person1 = Person("yuli_person")
student1 = Student("yuli_student","CS", "one")
teacher1 = Teacher("yuli_teacher",["C++", "Python"])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
		

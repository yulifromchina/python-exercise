#!/usr/bin/env python3 
n = int(input("Enter the number of students:"))
data = {}
Subjects = ('Physics', 'Math', 'History')
for i in range(0,n):
	name = input('Enter the  name of students {}:'.format(i+1))
	mark = []
	for x in Subjects:
		mark.append(int(input('Enter marks of {}:'.format(x))))
	data[name] = mark

for x,y in data.items():
	total = sum(y)
	print("{}'s total marks {}".format(x, total))
	if total < 120:
		print(x, 'failed :(')
	else:
		print(x, 'passed :)')

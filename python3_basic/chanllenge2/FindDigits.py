#!/usr/bin/env python3

file = open("./String.txt")
all_the_text = file.read()
new_string = ""
for x in all_the_text:
	if(x.isdigit()):
		new_string+=x
print(new_string)
	

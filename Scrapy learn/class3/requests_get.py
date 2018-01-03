#!usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup

res = requests.get('http://www.shiyanlou.com/courses/')
soup = BeautifulSoup(res.text,'lxml')
course = soup.find_all('div',{'class':'col-md-3','class':'col-sm-6','class':'course'})
for i in course:
	title = i.find('div',{'class':'course-name'}).get_text()
	study_people = i.find('span',{'class':'course-per-num','class':'pull-left'}).get_text()
	study_people = re.sub('\D',"", study_people)
	try:
		tag = i.find('span',{'class':'course-money','class':'pull-right'}).get_text()
	except:
		try:
			tag = i.find('span',{'class':'course-bootcamp','class':'pull-right'}).get_text()
		except:
			tag = '普通课程'

	print('{}  学习人数:{}	{}'.format(tag, study_people, title))

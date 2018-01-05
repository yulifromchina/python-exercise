#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup

host_url = 'http://www.shiyanlou.com{}'

course_count = 0
study_num = 0

def get_course_link(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text,'lxml')
	course =soup.find_all('div',{'class':'col-md-3','class':'col-sm-6','class':'course'})
	for i in course:
		global course_count
		global study_num
		course_count = course_count+1
		href = i.find('a',{'class':'course-box'}).get('href')
		title = i.find('div',{'class':'course-name'}).get_text()
		study_people = i.find('span',{'class':'course-per-num','class':'pull-left'}).get_text()
		study_people = re.sub('\D','',study_people)
		study_num = study_num + int(study_people)
		try:
			tag = i.find('span',{'class':'course-money','class':'pull-right'}).get_text()
		except:
			try:
				tag = i.find('span',{'class':'course-bootcamp','class':'pull-right'}).get_text()
			except:
				tag = '普通课程'
		print ('{}  学习人数:{}  {}   课程链接:{}'.format(tag, study_people, title, host_url.format(href)))

def main():
	res = requests.get('http://www.shiyanlou.com/courses/')
	soup = BeautifulSoup(res.text, 'lxml')
	course_link = 'http://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
	page = soup.find_all('ul',{'class':'pagination'})
	if len(page)<1:
		print ('未获得全部页面')
		return None
	li_tag= page[0].find_all('li')
	max_page= 0
	for i in li_tag:
		try:
			li_content = int(i.find('a').get_text())
		except:
			li_content = 0
		if li_content > max_page:
			max_page = li_content
	#print ('课程的最大页码：{}'.format(max_page))
	for i in range(1,max_page+1):
		get_course_link(course_link.format(i))
if __name__ == '__main__':
	main()
	print ('课程总数:{}  学习总次数:{}'.format(course_count, study_num))

#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
import time
import logging

logger = logging.getLogger()
formatter=logging.Formatter('%(asctime)s %(funcName)s %(levelname)-8s: %(message)s')
file_handler=logging.FileHandler('get_course_ex.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

host_url = 'http://www.shiyanlou.com{}'


def write_file(string):
	log =  open('spiders.log','a')
	log.write(string)
	log.write('\n')
	log.close()


def parse_content(url, title, tag, study_num):
	write_file('课程链接:{}'.format(url))
	logging.info(url)
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'lxml')
	type_list = soup.select('ol[class=breadcrumb] > li > a')
	types = []
	for i in type_list:
		if type_list.index(i)!=0 and type_list.index(i)!=len(type_list)-1:
			types.append(i.get_text())
	info = soup.find('div',{'class':'course-infobox-content'})
	try:
		info= info.find('p').get_text()
	except:
		info = '无介绍'
	teacher_name = soup.find('div',{'class':'name'})
	try:
		teacher_name = teacher_name.find('strong').get_text()
	except:
		teacher_name = '匿名'
	labs = soup.find('div',{'id':'labs'})
	test_list = labs.find_all('div',{'class':'lab-item'})
	tests_name = []
	for i in test_list:
		name = i.find('div',{'class':'lab-item-title'}).get_text()
		tests_name.append(name)
	write_file('课程名:{}'.format(title))
	write_file('老师:{}'.format(teacher_name))
	write_file('学习人数:{}'.format(study_num))
	write_file('课程标签:{}'.format(tag))
	write_file('课程所属类别:{}'.format('&'.join(types)))
	write_file('课程简介:{}'.format(info))
	write_file('课程章节：')
	for i in tests_name:
		write_file(str(i))
	write_file('*'*100)


def get_course_link(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text,'lxml')
	course = soup.find_all('div',{'class':'col-md-3','class':'col-sm-6','class':'course'})
	for i in course:
		href = i.find('a',{'class':'course-box'}).get('href')
		title = i.find('div',{'class':'course-name'}).get_text()
		study_people = i.find('span',{'class':'course-per-num','class':'pull-left'}).get_text()
		study_people = re.sub('\D','', study_people)
		try:
			tag = i.find('span',{'class':'course-money','class':'pull-right'}).get_text()
		except:
			try:
				tag = i.find('span',{'class':'course-bootcamp','class':'pull-right'}).get_text()
			except:
				tag = '普通课程'
		logging.debug(href)
		logging.debug(host_url.format(href))
		parse_content(url = host_url.format(href),title = title, tag = tag, study_num = study_people)
		time.sleep(0.5)


def main():
	res = requests.get('http://www.shiyanlou.com/courses/')
	soup = BeautifulSoup(res.text, 'lxml')
	course_link = 'http://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
	page = soup.find_all('ul',{'class':'pagination'})
	if len(page)<1:
		logging.error('未获取全部页面')
		return 
	li_content = page[0].find_all('li')
	max_page = 0
	for i in li_content:
		try:
			page_num=int(i.find('a').get_text())
		except:
			logging.error('获取到的是:{}'.format(i.find('a').get_text()))
			page_num = 0
		if max_page < page_num:
			max_page = page_num
	logging.debug('最大页数：{}'.format(max_page))
	for i in range(1,max_page+1):
		write_file('【页码】:{}'.format(i))
		get_course_link(course_link.format(i))


if __name__=='__main__':
	main()

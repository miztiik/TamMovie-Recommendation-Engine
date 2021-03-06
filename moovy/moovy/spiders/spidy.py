#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
import itertools
import collections
from moovy.items import MoovyItem

# General generator function that skips any number of items from the beginning and end of an iterable
# http://stackoverflow.com/questions/10079216/skip-first-entry-in-for-loop-in-python
def skip(iterable, at_start=0, at_end=0):
	it = iter(iterable)
	for x in itertools.islice(it, at_start):
		pass
	queue = collections.deque(itertools.islice(it, at_end))
	for x in it:
		queue.append(x)
		yield queue.popleft()


class MoovySpider(scrapy.Spider):
    name = "moovy"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_Tamil_films_of_2015"]
				
    def parse(self,response):
		rows = response.selector.xpath('//table[@class="wikitable sortable"]/tr')
		for index, r1 in enumerate(rows):
			mData = []
			cells = r1.xpath('.//td')
			# Lets remove the last wiki column as that only has reference			
			if (len(cells) == 8):
				#print ("This row has {} cells and month is {}".format(len(cells),str(cells[0].xpath('.//text()').extract())))
				mMonth = cells[0].xpath('.//text()').extract()
				# Remove any new line characters from the list  & use map to join the list into single string.
				mMonth = map(lambda s: s.strip(), mMonth)
				mMonth = ''.join(map(str,mMonth))
				
				mWeek = cells[1].xpath('.//text()').extract()
				# Remove any new line characters from the list  & use map to join the list into single string.
				mWeek = map(lambda s: s.strip(), mWeek)
				mWeek = ''.join(map(str,mWeek))
				# print ("This row has {} cells and released on the month of {} , week ending {}".format(len(cells), mMonth, mWeek))
				# Lets skip the first two cells (Month & Week) and the last one (Wiki Ref Link)
				cells = list(skip(cells,at_start=2,at_end=1))
			elif (len(cells) == 7):
				mWeek = cells[0].xpath('.//text()').extract()
				# Remove any new line characters from the list  & use map to join the list into single string.
				mWeek = map(lambda s: s.strip(), mWeek)
				mWeek = ''.join(map(str,mWeek))
				# print ("This row has {} cells and released on week ending {}".format(len(cells), mWeek))
				# Lets skip the first cell (Week) and the last one (Wiki Ref Link)
				cells = list(skip(cells,at_start=1,at_end=1))
			else:
				# print ('This row has %s cells' % len(cells))
				# Lets skip the last one (Wiki Ref Link)
				cells = list(skip(cells,at_start=0,at_end=1))
			
			# Enumerate over the media Title, Director, Cast, Genre & Production House
			for cc,c1 in enumerate(cells):
				data = c1.xpath('.//text()').extract()
				data = [s.replace('\n',', ') for s in data]
				mData.append(''.join(map(str, data)))
				#print ('Month:{} , Week:{} , in this cell is {}'.format(mMonth,mWeek,''.join(map(str, data))))
			
			# Check if the movie data is not empty and print out the list with "|" separated line
			if mData:
				print ('{}|{}|{}'.format(mMonth,mWeek,'|'.join(map(str, mData))))
			else:
				print ('Unable to extract data')
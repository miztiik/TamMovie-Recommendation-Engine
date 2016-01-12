import scrapy

from moovy.items import MoovyItem

class MoovySpider(scrapy.Spider):
        name = "moovy"
        allowed_domains = ["en.wikipedia.org"]
        start_urls = ["https://en.wikipedia.org/wiki/List_of_Tamil_films_of_2015"]

        def parse(self,response):
			#titles = response.selector.xpath('//table[@class="wikitable sortable"]/tr/td/i/a[contains(@href, "title")]')
			rows = response.selector.xpath('//table[@class="wikitable sortable"]/tr')

			for index, r1 in enumerate(rows):
				#cells = r1.xpath('.//td').extract()
				c1 = r1.css('td')
				#print cells
				print('This is my text %s' % c1)
				
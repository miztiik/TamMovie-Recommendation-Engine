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
				cells = r1.xpath('.//td')
				if (len(cells) == 8):
					#print ("This row has {} cells and month is {}".format(len(cells),str(cells[0].xpath('.//text()').extract())))
					str1 = cells[0].xpath('.//text()').extract()
					str1 = map(lambda s: s.strip(), str1)
					str1 = ''.join(map(str,str1))
					print ("This row has {} cells and month is {}".format(len(cells), str1))
					#print("Total score for {} is {}".format(name, score))
				else:
					print ('This row has %s cells' % len(cells))
				for cc,c1 in enumerate(cells):
					data = c1.xpath('.//text()').extract()
					print ('This data in this cell is %s' % ''.join(map(str, data)))
				#print ('End of row')

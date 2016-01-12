import scrapy

class MoovyItem(scrapy.Item):
        title = scrapy.Field()
        link = scrapy.Field()
        desc = scrapy.Field()

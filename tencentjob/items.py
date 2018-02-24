# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentjobItem(scrapy.Item):
    title = scrapy.Field()
    location = scrapy.Field()
    classify = scrapy.Field()
    count = scrapy.Field()
    duty = scrapy.Field()
    requirement = scrapy.Field()
    link = scrapy.Field()
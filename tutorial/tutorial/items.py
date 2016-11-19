# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    issue = scrapy.Field()
    date = scrapy.Field()
    sales_of_this_issue = scrapy.Field()
    jackpot = scrapy.Field()
    numbers = scrapy.Field()
    prize_info = scrapy.Field()
    


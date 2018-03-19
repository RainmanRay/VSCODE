# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

class SunmoiveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cate_url = Field()
    cate_name = Field()
    cat_url_list = Field()
    movie_name = Field()
    movie_url = Field()
    movie_source = Field()


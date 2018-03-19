# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class LuyiluItem(scrapy.Item):
    title = Field()
    img_url = Field()
    url = Field()
class LuyiluImgItem(scrapy.Item):
    title = Field()
    img_url = Field()
    url = Field()
    #cat = Field()

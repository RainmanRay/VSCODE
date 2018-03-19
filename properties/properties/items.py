# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field, Item


class PropertiesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    price = Field()
    description = Field()
    address = Field()
    image_urls = Field()
    vot=Field()

    images = Field()
    location = Field()


    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()


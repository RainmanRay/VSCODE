# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.exceptions import DropItem

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from luyilu.settings import IMAGES_STORE

import re

import scrapy
import json

# class LuyiluPipeline(object):
#     def process_item(self, item, spider):
#         with open('data.txt','r+') as f:
#             lines = f.readlines()
#             for line in lines:
#                 line.split('|')[0]
#
#             return item

class LuImagePipeline(ImagesPipeline):


    def get_media_requests(self, item, info):
        for image_url in item['img_url']:
            referer = item['url']
            #self.dir_name.append(item['title'])
            yield scrapy.Request(image_url,meta={'item':item, 'referer':referer})
    #
    # def item_completed(self, results, item, info):
    #     img_paths = [x['path'] for ok, x in results if ok]
    #     if not img_paths:
    #         return  DropItem("item contains no images...")

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']

        folder = item['title']
        #cat = item['cat']
        folder_strip = self.strip(folder)
        #
        # if cat == '16':
        #     typ = 'Asian'
        # elif cat == '18':
        #     typ = 'SLeg'
        # elif cat == '20':
        #     typ = 'Beauty'
        # elif cat == '23':
        #     typ = 'SWM'
        # else:
        #     typ = 'Other'

        img_guid = request.url.split('/')[-1].split('-')[-1]

        filename = r'/{}/{}'.format(folder_strip,img_guid)
        #filename = r'/{0}/{1}/{2}'.format('Asian',folder_strip,img_guid)
        # filename = r'{0}/{1}'.format('Beauty', img_guid)
        return filename

    def strip(self,path):
        paths = re.sub(r'[？\\*|“<>:/]', '', str(path))

        return paths
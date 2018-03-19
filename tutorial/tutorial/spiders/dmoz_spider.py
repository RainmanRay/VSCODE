import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem
import sys


sys.path.append(r"D:\vscode\tutorial\tutorial")




class DmozSpider(Spider):
    name = 'dmoz'
    start_url = ["https://www.haha.mx/topic/1/new/1"]

    def parse(self, response):
        sel = Selector(response)
        #print(response.body)
        wrapers = sel.xpath('//div[@class="joke-list-item-main"]')
        items = []
        for wrap in wrapers:
            img_url = wrap.xpath(
                './div[@class="joke-main-content clearfix"]/a/img/@src').extract()
            #sel.xpath('//div[@class="joke-list-item-main"]/div[@class="joke-main-content clearfix"]/a/img/@src').extract()
            img_cont = wrap.xpath(
                './div[@class="joke-main-content clearfix"]/p/text()').extract()
            img_vote = wrap.xpath(
                './div/div[@class="joke-main-misc clearfix"]/div[1]/a[1]/text()').extract()

            item = DmozItem()

            item['link'] = img_url
            item['title'] = img_cont
            item['desc'] = img_vote
            items.append(item)
            print(img_url)
        return items
'''
class DmozItem(scrapy.Item):
    title=scrapy.Field()
    link=scrapy.Field()
    desc=scrapy.Field()        
'''
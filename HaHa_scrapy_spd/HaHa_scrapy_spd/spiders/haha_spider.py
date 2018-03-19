import sys
sys.path.append(R'D:\VSCODE\HaHa_scrapy_spd\HaHa_scrapy_spd')
import scrapy
from HaHa_scrapy_spd.items import HahaScrapySpdItem
from scrapy.selector import Selector




class HaSpider(scrapy.Spider):
    name = 'haha'


def start_requests(self):

    start_urls = [
        "https://www.haha.mx/topic/1/new/"
    ]
    for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


def parse(self, response):
    items = []
    htmlCont = Selector(response)
    xConts = htmlCont.xpath('//div[@class="joke-main-content clearfix"]')
    for xCont_each in xConts:
         xItem = HahaScrapySpdItem()
         xItem['comm'] = xCont_each.xpath('/div/p/text()').extract()
         xItem['img_url'] = xCont_each.xpath('/a/img/@src').extract()
         xItem['vot']['good'] = xCont_each.xpath(
             '../div/div/div/a[@data="g"]/text()').extract()
         xItem['vot']['bad'] = xCont_each.xpath(
             '../div/div/div/a[@data="b"]/text()').extract()
         xItem['vot']['comm'] = xCont_each.xpath(
             '../div/div/div//a[@data="c"]/text()').extract()
         print(xItem['comm'])
         items.append(xItem)

    return items

import scrapy
from scrapy.spider import Spider
from luyilu.items import LuyiluImgItem

class TestSipder(Spider):
    name = 'Test'
    start_urls = ['http://yxpjwnet1.com']
def parse(self, response):
    item = LuyiluImgItem()
    item['url'] = response.url
    request = scrapy.Request("http://yxpjwnet1.com/page/1.html",
                             callback=self.parse_page2)
    request.meta['item'] = item
    yield request

def parse_page2(self, response):
    item = response.meta['item']
    item['other_url'] = response.url
    yield item


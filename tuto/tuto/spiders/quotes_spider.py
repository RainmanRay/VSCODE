import scrapy
import sys
from scrapy.selector import Selector
from tuto.items import TutoItem

sys.path.append('D:\\VSCODE\\tuto\\tuto\\')


class QuotesSpider(scrapy.Spider):
    name = "qu"

    def start_requests(self):
        urls = [
            'https://www.haha.mx/topic/1/new/1/',
            'https://www.haha.mx/topic/1/new/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)'''
        item = []
        htmlCont = Selector(response)
        xConts = htmlCont.xpath('//div[@class="joke-list-item-main"]')
        for xCont_each in xConts:
            xItem = TutoItem()
            xItem['comm'] = xCont_each.xpath('div[@class="joke-main-content clearfix"]/p/text()').extract_first()

            xItem['img_url'] = xCont_each.xpath('div/a/img/@src').extract_first()
            xItem['vot'] = xCont_each.xpath('div/div/div/a[@data="g"]/text()')[0].extract()
            # xItem['vot']['bad'] = xCont_each.xpath(‘//div/div/div/a[@data="b"]/text()').extract()
            # xItem['vot']['comm'] = xCont_each.xpath('//div/div/div//a[@data="c"]/text()').extract()
            item.append(xItem)
            print(xItem['comm'])
        yield item



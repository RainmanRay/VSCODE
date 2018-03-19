# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.http import Request

from scrapy.loader import ItemLoader

from properties.items import PropertiesItem

from scrapy.loader.processors import MapCompose,Join


class BasicSpider(scrapy.Spider):
    name = "basic"
    #allowed_domains = ["web"]
    start_urls = ('https://www.haha.mx/topic/1/new/1/',)

    #start_urls = [url.strip() for url in open(R'D:\VSCODE\properties\properties\todo.urls.txt').readlines()]
    #def parse(self, response):
        # item = PropertiesItem()
        # item['title'] = response.xpath('//*[@itemprop="name"][1]/text()').extract()
        # item['price'] = response.xpath('//*[@itemprop="price"][1]/text()').re('[.0-9]+')
        # item['description'] = response.xpath('//*[@itemprop="description"][1]/text()').extract()
        # item['address'] = response.xpath('//*[@itemtype="http://schema.org/''Place"][1]/text()').extract()
        # item['image_urls'] = response.xpath('//*[@itemprop="image"][1]/@src').extract()
        # return item
        # for url in open(R'D:\VSCODE\properties\properties\todo.urls.txt').readlines():
        #     print(url.strip())


        # I = ItemLoader(item=PropertiesItem(), response=response)
        # I.add_xpath('title', '//div[@class="joke-main-content clearfix"]/p/text()',MapCompose(lambda i:i.replace('分享图片','')))
        # #I.add_xpath('price', '//*[@itemprop="price"][1]/text()')
        # I.add_xpath('description','//div/div/div/a[@data="g"]/text()')
        # #I.add_xpath('address','//*[@itemtype="http://schema.org/''Place"][1]/text()')
        # I.add_xpath('image_urls','//a/img[@class="joke-main-img"]/@src')
        #
        # return I.load_item()

        # next_selector = response.xpath('//a[@class="pagination-link pagination-next"]/@href').extract()
        # for each_next_selector in next_selector:
        #     yield Request('https://www.haha.mx'+each_next_selector,callback=self.parse_pageItem,method='GET')
        # item_serlector = response.xpath('//div[@class="joke-list-item-main"]')
        # for url in item_serlector.extract():
        #     yield  Request

    def parse(self, response):

    # Get the next index URLs and yield Requests
        next_selector = response.xpath('//*[contains(@class,'
                                   '"next")]//@href')

        for url in next_selector.extract():
            yield Request(urlparse.urljoin(response.url, url))
    # Get item URLs and yield Requests
        item_selector = response.xpath('//*[@itemprop="url"]/@href')
        for url in item_selector.extract():
            yield Request(urlparse.urljoin(response.url, url),callback=self.parse_item)
    def parse_pageItem(self,response):
        item = PropertiesItem()
        # item['title'] = response.xpath('//*[@itemprop="name"][1]/text()').extract()
        # item['price'] = response.xpath('//*[@itemprop="price"][1]/text()').re('[.0-9]+')
        # item['description'] = response.xpath('//*[@itemprop="description"][1]/text()').extract()
        # item['address'] = response.xpath('//*[@itemtype="http://schema.org/''Place"][1]/text()').extract()
        # item['image_urls'] = response.xpath('//*[@itemprop="image"][1]/@src').extract()
        sel = Selector(response)
        xConts =sel.xpath('//div[@class="joke-list-item-main"]')
        for xCont_each in xConts:
            item['description'] = xCont_each.xpath('//div[@class="joke-main-content clearfix"]/p/text()').extract()
            item['image_urls'] = xCont_each.xpath('//a/img[@class="joke-main-img"]/@src').extract()
            item['vot'] = xCont_each.xpath('//div/div/div/a[@data="g"]/text()').extract()
            # xItem['vot']['bad'] = xCont_each.xpath(‘//div/div/div/a[@data="b"]/text()').extract()
            # xItem['vot']['comm'] = xCont_each.xpath('//div/div/div//a[@data="c"]/text()').extract()
            next_selector = response.xpath('//a[@class="pagination-link pagination-next"]/@href').extract()
            for each_next_selector in next_selector:
                Request('https://www.haha.mx' + each_next_selector, callback=self.parse_pageItem, method='GET')
            yield item






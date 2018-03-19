
import sys
sys.setdefaultencoding = 'uft-8'
from scrapy import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from luyilu.items import LuyiluImgItem
from scrapy.linkextractors import LinkExtractor
import re

class LuyiluSpider(CrawlSpider):
    name = 'Luyilu'
    # allowd_domain = ['yxpjwnet3.com']
    base_url = 'http://yxpjwnet3.com'
    
    start_urls = {'http://yxpjwnet3.com/page/1.html',}

    rules =(Rule(LinkExtractor(allow=('http://yxpjwnet3.com/.*',),deny=('youfanhao/','qiuchuchu/','xiachedan/',),), callback= 'parse_main'),)

    # def start_requests(self):
    #
    #     # yield Request(
    #     #     self.base_url+ '/page/1.html', dont_filter=True, meta={'dont_redirect': True, "handle_httpstatus_list": [302]}, callback=self.parse)
    #     yield Request(
    #         self.base_url + '/page/1.html', callback=self.parse)

    def get_mainPage_urls(self, response):
        sel = Selector(response)
        #Main page to fetch next page
        #img_urls = sel.xpath('//a[contains(@href,"/20")]/@href').extract()

        img_urls = sel.xpath('//a[contains(@href, "/201") and not(contains(@title, "PLAYBOY"))]/@href').extract()
        
        return img_urls

    def get_next_mainpage(self, response):
        return str(Selector(response).xpath('//li[@class="next-page"]/a/@href').extract_first())

    def parse_main(self, response):
        # main_page_urls = Selector(response).xpath(
        #     '//a[contains(@href,"/20") and not(@class="thumbnail") and not(contains(@title, "PLAYBOY")]/@href').extract()
        main_page_urls = self.get_mainPage_urls(response)
        for url in main_page_urls:
            yield Request(self.base_url + url, callback=self.parse_subPage)
        yield Request(self.base_url+ '/page/' + self.get_next_mainpage(response), callback=self.parse_main)



    def parse_subPage(self, response):
        item = LuyiluImgItem()

        item['img_url'] = Selector(response).xpath('//img[contains(@src,"images.") and not(@class="thumb")]/@src').extract()
        cur_title= Selector(response).xpath('//h1/text()').extract_first()
        par = re.compile('\(\d*\)')
        rst = par.findall(cur_title)
        if len(rst) > 0:
            rst = rst[0]
        else:rst = ''
        item['title'] = cur_title.replace(rst,'')
        item['url'] = response.url
        next_suburl = Selector(response).xpath('//li[@class="next-page"]/a/@href').extract_first(default=None)
        if not next_suburl == None:
            next_pagurl = response.url.replace(response.url.split('/')[-1], next_suburl)
        else:
            next_pagurl = response.url

        yield Request(next_pagurl, callback= self.parse_subPage)
        yield item
        rela_url = Selector(response).xpath('//a[contains(@href,"/20")]/@href').extract()
        for url in rela_url:
            par = re.compile('youfanhao')
            par2 =re.compile('xiurenwang')
            third_par = re.compile('youmihui')
            chedan = re.compile('xiachedan')
            chuchu = re.compile('chuchu')
            no_true = len(par.findall(url)) + len(par2.findall(url)) + len(third_par.findall(url))
            no_true += len(chedan.findall(url)) + len (chuchu.findall(url))
            if no_true == 0:
                yield Request('http://yxpjwnet1.com'+url, callback = self.parse_subPage)




#
# import sys
# sys.setdefaultencoding = 'uft-8'
# from scrapy import Selector
#
#
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.http import Request
# from luyilu.items import LuyiluImgItem
# from scrapy.linkextractors import LinkExtractor
#
# class LuyiluSpider(CrawlSpider):
#     name = 'Luyilu'
#     allowd_domain = ['www.46ek.com']
#     base_url = 'http://www.46ek.com'
#     start_urls = ['http://www.46ek.com/html/part/20.html']
#     rules =(
#             Rule(
#             LinkExtractor(allow='http://www.46ek.com/html/part/[(16)(18)(20)(23)].*\.html',),
#             callback = 'parse_main'),
#             )
#
#     def get_mainPage_urls(self, response):
#         sel = Selector(response)
#         img_urls = sel.xpath('//a[contains(@href,"/html/article/")]/@href').extract()
#         return img_urls
#
#     def get_next_mainpage(self, response):
#         return Selector(response).xpath('//a[contains(text(),"下一页")]/@href').extract_first()
#
#     def parse_main(self, response):
#         main_page_urls = self.get_mainPage_urls(response)
#         for url in main_page_urls:
#             yield Request(self.base_url + url, callback=self.parse_subPage,meta = {'src':response.url,})
#         yield Request(self.base_url+self.get_next_mainpage(response), callback=self.parse)
#
#     def parse_subPage(self, response):
#         item = LuyiluImgItem()
#         main_type = response.meta['src'].split('/')[-1][:2]
#         item['cat'] = main_type
#         item['img_url'] = Selector(response).xpath('//div[@class ="n_bd"]/img/@src').extract()
#         item['title']  = Selector(response).xpath('//div[@class="title"]/text()').extract_first()
#         item['url'] = response.url
#         yield item
#
#
#
#

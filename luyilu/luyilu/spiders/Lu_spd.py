# from __future__ import division
#
# import json
# import sys
# sys.setdefaultencoding = 'uft-8'
#
# import pickle
#
#
#
# from scrapy import Selector
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.http import Request
# from luyilu.items import LuyiluImgItem
# from scrapy.linkextractors import LinkExtractor
# import os
# import re
#
# class LuyiluSpider(CrawlSpider):
#     name = 'Luyilu'
#     allowd_domain = ['yxpjwnet1.com']
#     page_imgs_urls= {}
#
#     def start_requests(self):
#         rules = Rule(
#             LinkExtractor(allow='http://yxpjwnet1.com/page/\d\\+.html', deny='http://i.imgur.com/H1ThoZf.jpg')
#         )
#         yield Request('http://yxpjwnet1.com/page/1.html'
#                       '', dont_filter=True, meta={'dont_redirect': True, "handle_httpstatus_list": [302]},
#                       callback=self.parse_conn)
#
#     def parse_conn(self, response):
#         return Request(response.url, callback=self.parse)
#
#
#     def get_mainPage_urls(self, response):
#         sel = Selector(response)
#         img_urls = sel.xpath('//a[contains(@href,"/20")]/@href').extract()
#         return img_urls
#
#     def get_next_mainpage(self, response):
#         return str(Selector(response).xpath('//li[@class="next-page"]/a/@href').extract_first())
#
#     def parse(self, response):
#         main_page_urls = Selector(response).xpath(
#             '//a[contains(@href,"/20") and not(@class="thumbnail")]/@href').extract()
#         for url in main_page_urls:
#             yield Request('http://yxpjwnet1.com' + url, callback=self.parse_subPage)
#         yield Request(r'http://yxpjwnet1.com/page/' + self.get_next_mainpage(response), callback=self.parse)
#
#     def push_mainpages(self, response):
#
#         start_page = 1
#         start_page += start_page
#
#
#     def parse_start(self, response):
#         self.parse(response)
#         return None
#
#     def parse_subPage(self, response):
#         item = LuyiluImgItem()
#
#         img_urls = Selector(response).xpath('//img[contains(@src,"images.") and not(@class="thumb")]/@src').extract()
#         item['title'] = Selector(response).xpath('//h1/text()').extract_first()
#         item['url'] = response.url
#         self.page_imgs_urls[item['title']] = []
#         # item['img_url'] = img_urls
#         pars = re.compile('\[\d{2,3}\S\]')
#         par = pars.findall(item['title'])[0]
#         pages_num = re.search(r'\d{2,3}', par).group()
#         rge = round(int(pages_num) / 5 + 1)
#         for index in range(1, rge):
#             if int(response.status) == 302:
#                 return None
#
#             if index >= 2:
#                 tar_url = response.url.replace('.html', '_{0}.html'.format(index))
#                 req =Request(url=tar_url, callback=self.craw_sub_page_img_urls)
#                 req.meta['title'] = item['title']
#                 req.meta['count'] = index +1
#                 req.meta['rge'] = rge
#                 yield req
#
#             else:
#                 src_url = response.url
#                 yield Request(url=(src_url), callback=self.craw_sub_page_img_urls)
#
#         # with open('data.json','w') as f:
#         #     pickle.load(f)
#         #     print(f[item['title']])
#         yield item
#         # item['img_url'] = self.page_imgs_urls
#         # # item['img_url'].remove([])
#         # self.page_imgs_urls.clear()
#         # yield item
#
#     def craw_sub_page_img_urls(self, response):
#         title = response.meta['title']
#         count = response.meta['count']
#         rge = response.meta['rge']
#         img_urls = Selector(response).xpath('//img[contains(@src,"images.") and not(@class="thumb")]/@src').extract()
#
#         for url in img_urls:
#             self.page_imgs_urls[title].append(url)
#
#             with open('data.txt', 'ab') as f:
#                 f.write(str(title+'|'+url+'\n').encode('utf-8'))
#
#

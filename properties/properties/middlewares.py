# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from properties.user_agent import agents


class UserAgentMiddleware(object):

    def process_request(self,request,spider):
        agent = random.choice(agents)
        request.headers['User-Agent'] = agent


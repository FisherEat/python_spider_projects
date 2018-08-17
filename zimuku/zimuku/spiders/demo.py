# -*- coding: utf-8 -*-
"""
参考文献 知乎-从零开始写ython爬虫: https://zhuanlan.zhihu.com/p/26854842

"""

import scrapy
from zimuku.items import ZimukuItem

class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['zimuku.net']
    start_urls = ['http://zimuku.net/']

    def parse(self, response):
        name = response.xpath('//b/text()').extract()[1]
        items = {}
        items['第一个'] = name
        return items

# -*- coding: utf-8 -*-
__author__ = 'zg'
from scrapy.spider import BaseSpider


class testSpider(BaseSpider):
    name = "test"
    allowed_domains = ["whpu.edu"]
    start_urls = [
        "http://www,whpu.edu.cn"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
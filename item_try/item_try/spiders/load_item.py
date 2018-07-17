# -*- coding: utf-8 -*-
import scrapy


class LoadItemSpider(scrapy.Spider):
    name = 'load_item'
    allowed_domains = ['backpackers.com.tw']
    start_urls = ['http://backpackers.com.tw/']

    def parse(self, response):
        pass

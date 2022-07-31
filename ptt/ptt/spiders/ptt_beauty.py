# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import requests
from scrapy_selenium import SeleniumRequest
import time
from ptt.items import PttItem


class PttBeautySpider(scrapy.Spider):
    name = 'ptt_beauty'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Beauty/index.html']


    def parse(self, response):
        for i in range(10):
            time.sleep(3)
            url = "https://www.ptt.cc/bbs/Beauty/index" + str(3999 - i) + ".html"
            yield scrapy.Request (url, cookies={'over18': '1'}, callback=self.parse_article)

    def parse_article(self, response):
        item = PttItem()
        soup = BeautifulSoup(response.text, "html.parser")
        for i in soup.select('.r-ent'):
            try :
                item['title'] = i.find('a').text
                item['date'] = i.select('.date')[0].text
                item['href'] = i.find('a').get('href')
                item['push'] = i.select('.nrec')[0].text

                yield item
            except IndexError :
                pass
            continue


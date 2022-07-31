import scrapy


class PttBeauty1Spider(scrapy.Spider):
    name = 'ptt_beauty1'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['http://www.ptt.cc/']

    def parse(self, response):
        pass

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PttItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 爬取文章標題、發文時間、推文數
    title = scrapy.Field()
    date = scrapy.Field()
    href = scrapy.Field()
    push = scrapy.Field()    
    pass

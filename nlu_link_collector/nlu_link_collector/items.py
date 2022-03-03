# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NluLinkCollectorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source_uri = scrapy.Field()
    year = scrapy.Field()
    volume = scrapy.Field()
    title = scrapy.Field()
    uri = scrapy.Field()

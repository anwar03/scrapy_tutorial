# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidermanItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()


class AmazonSpidermanItem(scrapy.Item):
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_price = scrapy.Field()
    book_image_url = scrapy.Field()

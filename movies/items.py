# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field()
    Abstract = scrapy.Field()
    Director = scrapy.Field()
    Type = scrapy.Field()
    Rate = scrapy.Field()
    Year = scrapy.Field()
    Rate_count = scrapy.Field()
    Poster_URL = scrapy.Field()

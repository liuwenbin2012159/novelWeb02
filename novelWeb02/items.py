# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item, Field
import scrapy


class NovelwebItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
pass


class NovelInfoItem(Item):
    # ID = Field()  # novel ID
    # origin = Field()  # origin
    # visitCount= Field()  # visit
    # visitCount = Field()  # visit
    novelName= Field()  # novelName
    author = Field()  # author
    novelTitle = Field()  # novelTitle
    type= Field()  # noveltype
    updateStatus= Field()  # updateStatus
    novelDesc= Field()  # novelDesc
    lasterChapterName= Field()  # lasterChapterName
    lasterChapterURL= Field()  # lasterChapterURL

class NoveContentItem(Item):
    # ID = Field()  # chapterID
    chapterURL= Field()  # chapterURL
    chapterContent= Field()  # chapterContent
    chapterName= Field()  # chapterName

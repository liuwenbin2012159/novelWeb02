# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo as pymongo
from novelWeb02.items import *

class NovelwebPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoDBPipleline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["novel_item"]
        self.novelDetail = db["novel_detail"]
        self.novelInfo = db["novel_info"]
        self.novelDesc = db["novel_desc"]
        self.novelContent = db["novel_content"]

    def process_item(self, item, spider):
        if isinstance(item, NovelInfoItem):
            try:
                self.Information.insert(dict(item))
            except Exception:
                pass
        elif isinstance(item, NoveContentItem):
            try:
                self.Tweets.insert(dict(item))
            except Exception:
                pass
        return item

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
from time import time

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
        item._values['status'] = 1
        item._values['createTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S');
        if isinstance(item, NovelInfoItem):
            try:
                novelID = self.novelInfo.insert(dict(item))
                item._values['novelID'] = novelID

            except Exception:
                pass
        elif isinstance(item, NoveContentItem):
            try:
                chapterID = self.novelContent.insert(dict(item))
            except Exception:
                pass
        return item

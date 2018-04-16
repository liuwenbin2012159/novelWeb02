# -*- coding: utf-8 -*-
BOT_NAME = 'NovelSpider'
SPIDER_MODULES = ['novelWeb02.spiders']
NEWSPIDER_MODULE = 'novelWeb02.spiders'
ROBOTSTXT_OBEY = True
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
ITEM_PIPELINES = {
    'novelWeb02.pipelines.MongoDBPipleline': 300,
}

REDIE_URL = None
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
DOWNLOAD_DELAY = 2
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

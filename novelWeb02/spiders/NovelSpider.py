from scrapy import Selector
from scrapy_redis.spiders import RedisSpider
import scrapy_redis
from scrapy.http import Request
from novelWeb02.items import *

class NovelSpider(RedisSpider):
    name = "novelSpider"
    # allowed_domains = ["dmoz.org"]

    redis_key = "novelSpider:novel_url"

    for i in range(10000):
        urlList ="http://www.kushubao.com/" + str(i) + "/";

    start_urls = urlList;

    def start_requests(self):
        for url in self.start_urls:
            print("url============="+url)
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        selector = Selector(response)
        novelInfoItem = NovelInfoItem();
        # ID = re.findall('weibo\.cn/(\d+)', response.url)[0]
        novelInfoItem['novelTitle']= selector.xpath('//*[@class="entry-single"]/h1')
        novelInfoItem['author']= selector.xpath('//*[@class="des"]/p/span')[0]
        novelInfoItem['novelStatus']= selector.xpath('//*[@class="des"]/p/span')[0]
        novelInfoItem['lasterChapter']= selector.xpath('//*[@class="des"]/p/a')
        novelInfoItem['novelStatus']= selector.xpath('//*[@class="des"]/p/a')
        novelInfoItem['lasterChapterName']= selector.xpath('//*[@class="des"]/p/a')
        novelInfoItem['lasterChapterURL']= selector.xpath('//*[@class="des"]/p/a/@href')
        novelInfoItem['type']= selector.xpath('//*[@class="des"]/p')[1]+selector.xpath('//*[@class="des"]/p')[2]+selector.xpath('//*[@class="des"]/p')[3]
        novelInfoItem['novelDesc'] = selector.xpath('//*[@class="des"]/p')[4]
        yield novelInfoItem

        chapterURLLiAry = selector.xpath('//*[@id="xslist"]/ul/li')
        for i in chapterURLLiAry:
            chapterURL = i.xpath('/a/@href')
            chapterTitle = i.xpath('/a/@title')
            yield Request(url=chapterURL, callback=self.parse2)


    def parse2(self, response):
        pass



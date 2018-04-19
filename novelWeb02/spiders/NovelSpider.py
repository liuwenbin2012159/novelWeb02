import logging

from scrapy import Selector
from scrapy_redis.spiders import RedisSpider
import scrapy_redis
from scrapy.http import Request
from novelWeb02.items import *


class NovelSpider(RedisSpider):
    start_urls = []
    logging.getLogger("requests").setLevel(logging.WARNING)  #

    name = "novelSpider"
    # allowed_domains = ["dmoz.org"]
    redis_key = "novelSpider:56_urls"
    #
    # start_urls = [
    #     "http://www.kushubao.com/1000/"
    # ]
    for i in range(10000):
        urlList = "http://www.kushubao.com/" + str(i) + "/";
        start_urls.append(urlList);

    # start_urls = [
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    # ]
    def start_requests(self):
        for url in self.start_urls:
            print("url=============" + url)
            yield Request(url=url, callback=self.parse)

    # def __init__(self, *args, **kwargs):
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(NovelSpider, self).__init__(*args, **kwargs)
    #     self.url = "http://www.kushubao.com/1000/"

    def parse(self, response):
        selector = Selector(response)
        novelInfoItem = NovelInfoItem();
        # ID = re.findall('weibo\.cn/(\d+)', response.url)[0]
        novelInfoItem['novelTitle'] = selector.xpath('//div[@class="entry-single"]/h1/text()').extract()[0]
        novelInfoItem['author'] = str(
            selector.xpath('//div[@class="des"]/p/span/b[1]/following::text()[1]')[0].extract()).replace('\xa0',
                                                                                                         '').replace(
            ' ', '');
        novelInfoItem['updateStatus'] = str(
            selector.xpath('//div[@class="des"]/p/span/b[2]/following::text()[1]')[0].extract()).replace('\xa0',
                                                                                                         '').replace(
            ' ', '');
        novelInfoItem['lasterChapterName'] = selector.xpath('//div[@class="des"]/p/a/text()').extract()[0]
        novelInfoItem['lasterChapterURL'] = str(selector.xpath('//div[@class="des"]/p/a/@href').extract()).replace(
            '\\r', '').replace('\\n', '').replace('\'', '').replace('[', '').replace(']', '')
        novelInfoItem['type'] = str(selector.xpath('//div[@class="des"]/p[2]/text()').extract()).replace('\\',
                                                                                                         '').replace(
            '\'', '').replace('[', '').replace(']', '')
        print(novelInfoItem['lasterChapterURL'])
        novelInfoItem['novelDesc'] = selector.xpath('//div[@class="des"]/p[5]/text()').extract()[0]

        yield novelInfoItem
        # chapterURLLiAry = selector.xpath('//div[@id="xslist"]/ul/li')
        chapterURL = selector.xpath('//div[@id="xslist"]/ul/li/a/@href').extract()
        for i in chapterURL:
            joinURL = ''.join(str(i).replace('\\r', '').replace('\\n', '').split())
            chapterID = str(joinURL).replace('http://www.kushubao.com/', '').replace('/', '')
            yield Request(url=joinURL, meta={'novelID': novelInfoItem._values['novelID'], 'chapterID': chapterID},
                          callback=self.parseContent,
                          dont_filter=True)

    def parseContent(self, response):
        selector = Selector(response)
        nove_content_item = NoveContentItem()
        nove_content_item['chapterID'] = response.meta['chapterID']
        nove_content_item['novelID'] = response.meta['novelID']
        nove_content_item['chapterContent'] = ''.join(selector.xpath('//div[@id="booktext"]/text()').extract())
        nove_content_item['chapterName'] = selector.xpath('//div[@class="entry-single"]/h1/text()').extract()[0]
        item = yield nove_content_item

        pass

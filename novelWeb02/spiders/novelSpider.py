import scrapy
from scrapy import log
class novelSpider(scrapy.Spider):
    name = "novelSpider"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://www.zhihu.com/question/20751219"
    ]

    def parse(self, response):
        print("result==="+str(response))
        filename = response.url.split("/")[-2]
        print("filename==="+str(filename))
        with open(filename, 'wb') as f:
            f.write(response.body)


    def parse_details(self, response):
        item = response.meta.get('item', None)
        if item:
            return item
        else:
            self.log('No item received for %s' % response.url,
                     level=log.WARNING)


    def closed(reason):
        print("closeed")
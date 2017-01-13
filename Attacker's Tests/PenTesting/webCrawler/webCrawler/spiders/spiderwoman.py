from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from webCrawler.items import BasicCrawlerItem
from scrapy.http import Request

class MySpider(BaseSpider):
    name = "webCrawler"
    allowed_domains = ['http://192.168.0.42']
    start_urls = ['http://192.168.0.42']

    def parse(self, response):
        hxs = Selector(response)

        #Enter code here to crawl!

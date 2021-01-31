import scrapy


class FirstSpiderDemoSpider(scrapy.Spider):

    # this is the exclusive identifier of the spider
    name = 'first_spider_demo'

    # specifies to whom spider can send requests
    # allowed_domains = ['www.baidu.com']

    # can have multiple urls
    start_urls = ['https://www.baidu.com/',
                  'https://www.sogou.com/']

    # parameter 'response' holds response obj
    def parse(self, response):
        print(response)

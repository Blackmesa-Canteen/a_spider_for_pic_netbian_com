import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        for div in div_list:

            # will return selector object list, but we need text!! Use extract() method
            author = div.xpath('./div[@class="author clearfix"]/a[1]/img/@alt').extract()[0]
            content_list = div.xpath('./a[@class="contentHerf"]/div/span//text()').extract()
            res_str = ''
            for str in content_list:
                res_str += str
            print(author, ' 说：', res_str)
            break


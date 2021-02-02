import scrapy

from qiuBaiSpider.qiuBaiSpider.items import QiubaispiderItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
    #     all_data = []
    #     for div in div_list:
    #
    #         # will return selector object list, but we need text!! Use extract() method
    #         author = div.xpath('./div[@class="author clearfix"]/a[1]/img/@alt').extract()[0]
    #         content_list = div.xpath('./a[@class="contentHerf"]/div/span//text()').extract()
    #         # res_str = ''
    #         # for str in content_list:
    #         #     res_str += str
    #         res_str = ''.join(content_list)
    #         print(author, ' 说：', res_str)
    #
    #         dic = {
    #             'author': author,
    #             'content': res_str
    #         }
    #         all_data.append(dic)
    #
    #     return all_data

    def parse(self, response):
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        all_data = []
        for div in div_list:

            # will return selector object list, but we need text!! Use extract() method
            author = div.xpath('./div[@class="author clearfix"]/a[1]/img/@alt').extract()[0]
            content_list = div.xpath('./a[@class="contentHerf"]/div/span//text()').extract()
            # res_str = ''
            # for str in content_list:
            #     res_str += str
            res_str = ''.join(content_list)

            item = QiubaispiderItem()
            item['author'] = author
            item['content'] = res_str

            yield item



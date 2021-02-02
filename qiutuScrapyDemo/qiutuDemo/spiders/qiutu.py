import scrapy


class QiutuSpider(scrapy.Spider):
    name = 'qiutu'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/imgrank/']

    # Since this site has many pages, I need a template of URL address:
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    page_num = 2

    def parse(self, response):
        img_url_list = []
        content_area_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        for element in content_area_list:
            img_url = 'https:' + element.xpath('./div[@class="thumb"]/a/img/@src').extract()[0]
            print(img_url)

        # recursive
        if self.page_num <= 5:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            # request manually
            yield scrapy.Request(url=new_url, callback=self.parse)

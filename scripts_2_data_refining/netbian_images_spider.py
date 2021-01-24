# -*- coding:utf-8 -*-
# @FileName  :netbian_images_spider.py
# @Time      :2021/1/24 11:31 AM
# @Author    :Xiaotian
import time
import random
import os

import requests
from lxml import etree

if __name__ == '__main__':
    url = "http://pic.netbian.com/4kdongwu/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
    }

    response = requests.get(url=url, headers=headers)
    # response.encoding = 'utf-8'
    page_text = response.text

    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    if not os.path.exists('../biantuImages'):
        os.mkdir('../biantuImages')

    for li in li_list:
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'

        # handle Garbled filename
        img_name = img_name.encode('iso-8859-1').decode('gbk')

        time.sleep(random.randint(2, 4))
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = '../biantuImages/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, "downloaded")





# -*- coding:utf-8 -*-
# @FileName  :SpiderFor58.py
# @Time      :2021/1/24 10:37 AM
# @Author    :Xiaotian
import requests
from lxml import etree

if __name__ == '__main__':
    url = "https://xj.58.com/ershoufang/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)

    res_list = tree.xpath('/html//h3[@class="property-content-title-name"]/text()')

    strings = ""
    for element in res_list:
        strings += element
        strings += "\n"

    with open('../texts/58fangchan.txt', 'w', encoding='utf-8') as fp:
        fp.write(strings)
    print('jobs done')
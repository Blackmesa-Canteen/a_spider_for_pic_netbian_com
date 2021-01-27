# -*- coding:utf-8 -*-
# @FileName  :getPopularCityName.py
# @Time      :2021/1/25 12:20 PM
# @Author    :Xiaotian
import requests
from lxml import etree
if __name__ == '__main__':
    url = "https://www.aqistudy.cn/historydata/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
    }

    pageText = requests.get(url=url, headers=headers).text
    tree = etree.HTML(pageText)
    hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    cityNames = []
    for li in hot_li_list:
        hotCityName = li.xpath('./a/text()')[0]
        cityNames.append(hotCityName)


    print(cityNames)
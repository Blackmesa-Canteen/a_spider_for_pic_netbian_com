# -*- coding:utf-8 -*-
# @FileName  :spider_pearVideo.py
# @Time      :2021/1/27 12:29 AM
# @Author    :Xiaotian
import requests
from lxml import etree
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
url = 'https://www.pearvideo.com/category_5'

# retrieve video page and video's name

if __name__ == '__main__':
    response_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(response_text)
    video_li_list = tree.xpath('//*[@id="listvideoListUl"]/li')

    for li in video_li_list:
        detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
        name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'

        print(detail_url, name)



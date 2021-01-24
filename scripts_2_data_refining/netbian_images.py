# -*- coding:utf-8 -*-
# @FileName  :netbian_images.py
# @Time      :2021/1/24 12:03 PM
# @Author    :Xiaotian

# memo
# I can handle Garbled filename by using:
# page_info = page_info.encode('iso-8859-1').decode('gbk')

import time
import random
import os

import requests
import re
from lxml import etree

# The steps for searching large images on the site http://pic.netbian.com/
# can be divided into three levels：
#
# Firstly, we send a query keyword to http://pic.netbian.com/e/search/index.php
# via POST, then the server returns a header that contains image_ID
# in this site.
#
# Then, we send the image_ID to http://pic.netbian.com/e/search/ with GET, the
# server will respond us with a html document contains several images we want.
# However, The resolution of these pictures is not high enough, we need to click
# hyperlinks attached to these images, which will redirect us to another web page
# that has bigger picture size. As a result, we need to store these hyperlinks.
# What's more, the original result page contains The page number information，we
# need to store it as well.
#
# When we get this information, we can download images one by one. All request
# operations are delayed by a few seconds to prevent a significant impact on
# server performance


# requires the HTML content of one of the search pages to'
# download all the large images that the current page contains
def downloadImagesOnThisPage(htmlText):
    treeObj = etree.HTML(htmlText)
    big_image_urls = treeObj.xpath('/html/body/div[2]/div/div[@class="slist"]/ul/li/a/@href')
    for url in big_image_urls:
        # target page contains the big image we need
        target_page_url = 'http://pic.netbian.com' + url
        print("waiting for request...")
        time.sleep(random.randint(2, 4))

        # prevent the gibberish in Chinese website: page_info.encode('iso-8859-1').decode('gbk')
        target_page_text = requests.get(url=target_page_url, headers=headers).text.encode('iso-8859-1').decode('gbk')
        print('request sent!')
        target_tree = etree.HTML(target_page_text)
        the_image_url = 'http://pic.netbian.com' + \
                        target_tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@src')[0]
        the_image_name = target_tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@title')[0] + '.jpg'

        the_image_content = requests.get(url=the_image_url, headers=headers).content
        with open('./' + keyword + '_images/' + the_image_name, 'wb') as fp:
            fp.write(the_image_content)
            print(the_image_name, 'downloaded')


if __name__ == '__main__':

    # this url requires ENGLISH image name and give us image id for searching
    query_imgId_url = "http://pic.netbian.com/e/search/index.php"

    # example: keyword = 'saber'
    keyword = input("what image do you want?\n")
    print("keyword confirmed:", keyword)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    query_data = {
        'keyboard': keyword,
        'submit': '',
        'tempid': '1',
        'tbname': 'photo',
        'show': 'title'
    }
    # id information is in the header['Location']
    query_response = requests.post(url=query_imgId_url, headers=headers, data=query_data, allow_redirects=False)
    query_response_headers_list = query_response.headers

    # if not found, exit
    if 'Location' not in query_response_headers_list.keys():
        print("sorry, not found... ...")
        exit(0)

    # create a folder
    if not os.path.exists('./' + keyword + '_images'):
        os.mkdir('./' + keyword + '_images')

    # requesting information
    print("located the image, waiting for searching to start...")
    image_Id_str = query_response_headers_list['Location']
    # retrieve pure number
    pattern = r'(?<=\?searchid=)[0-9]*'
    image_Id = int(re.findall(pattern, image_Id_str)[0])
    image_search_url = 'http://pic.netbian.com/e/search/' + image_Id_str
    time.sleep(random.randint(1, 2))
    print("searching started.\n")

    # use image id to search the image
    image_searchPage_text = requests.get(url=image_search_url, headers=headers).text
    tree = etree.HTML(image_searchPage_text)

    # find maximum pages
    end_page_str = tree.xpath('/html/body/div[2]/div/div[@class="page"]/a/text()')[-2]
    max_pages = int(end_page_str)

    print("There are " + end_page_str + " pages of images, ")
    # positive integer constraint
    pattern = r"^\+?[1-9][0-9]*$"

    while True:
        search_page_num_text = input("how many pages do you want to retrieve?\n")
        if re.match(pattern, search_page_num_text):
            if int(search_page_num_text) <= max_pages:
                break
        print("please input a positive integer which is not greater than", max_pages)

    # generating all search-result-page urls list
    res_page_url_list = []
    # this is page 1
    # res_page_url_list.append('http://pic.netbian.com/e/search/' + image_Id_str)
    # these are other pages
    for page_counter in range(1, int(search_page_num_text)):
        res_page_url_list.append('http://pic.netbian.com/e/search/result/index.php?page=' +
                                 str(page_counter) +
                                 '&searchid=' +
                                 str(image_Id))

    # now, in result image page, we retrieve all URLs to bigger images
    big_image_url_list = []

    # this is page 1, we have already got the xpath information about this page:
    downloadImagesOnThisPage(image_searchPage_text)

    # these are other pages
    for other_image_search_page_url in res_page_url_list:

        other_image_search_page_text = requests.get(url=other_image_search_page_url, headers=headers).text
        downloadImagesOnThisPage(other_image_search_page_text)
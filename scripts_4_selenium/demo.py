# -*- coding:utf-8 -*-
# @FileName  :demo.py
# @Time      :2021/1/29 2:11 PM
# @Author    :Xiaotian

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
from time import sleep

if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path="./geckodriver")
    driver.get("http://scxk.nmpa.gov.cn:81/xk/")

    page_text = driver.page_source

    tree = etree.HTML(page_text)

    element_list = tree.xpath('//*[@id="gzlist"]/li')

    for li in element_list:
        name = li.xpath('./dl/@title')[0]
        print(name)

    sleep(5)

    driver.quit()




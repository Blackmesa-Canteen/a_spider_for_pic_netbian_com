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
    driver.get('https://www.taobao.com')

    # find label
    search_input = driver.find_element_by_id('q')

    # automatically input
    search_input.send_keys('iPhone')

    # scroll
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(2)

    # find button and click it
    search_button = driver.find_element_by_css_selector('.btn-search')
    search_button.click()

    driver.get('https://www.baidu.com')
    sleep(2)

    driver.back()
    sleep(2)

    driver.forward()

    sleep(5)

    driver.quit()





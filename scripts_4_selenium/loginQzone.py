# -*- coding:utf-8 -*-
# @FileName  :loginQzone.py
# @Time      :2021/1/30 2:52 PM
# @Author    :Xiaotian
from selenium import webdriver
# headless
from selenium.webdriver.firefox.options import Options
from time import sleep


if __name__ == '__main__':
    firefoxOption = Options()
    firefoxOption.add_argument('--headless')
    firefoxOption.add_argument('--disable-gpu')

    driver = webdriver.Firefox(executable_path="./geckodriver", options=firefoxOption)

    driver.get('https://www.baidu.com')

    print(driver.page_source)
    sleep(2)
    driver.quit()


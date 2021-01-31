# -*- coding:utf-8 -*-
# @FileName  :demo.py
# @Time      :2021/1/29 2:11 PM
# @Author    :Xiaotian

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
from time import sleep
from selenium.webdriver import ActionChains

if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path="./geckodriver")
    driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

    # you can't do this directly, because this element exists in an iframe label!
    # div = driver.find_element_by_id('draggable')

    # you need to switch frame
    driver.switch_to.frame('iframeResult')
    # then
    div = driver.find_element_by_id('draggable')

    # ActionChain
    actionChain = ActionChains(driver)
    actionChain.click_and_hold(on_element=div)

    for i in range(5):
        actionChain.move_by_offset(17, 0).perform()
        sleep(0.3)

    actionChain.release()
    sleep(5)

    driver.quit()








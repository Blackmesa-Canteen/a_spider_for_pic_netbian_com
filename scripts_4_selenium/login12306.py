# -*- coding:utf-8 -*-
# @FileName  :login12306.py
# @Time      :2021/1/30 5:22 PM

from selenium import webdriver
# headless
from time import sleep
from chaojiying import *
import random
from PIL import Image
from selenium.webdriver import ActionChains


def get_track(distance):
    track = []
    current = 0
    mid = distance * 3 / 4
    t = 0.18
    v = 0
    while current < distance:
        if current < mid:
            a = random.uniform(1.8, 2.2)
        else:
            a = random.uniform(-3.2, -2.8)
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))

    return track


if __name__ == '__main__':

    driver = webdriver.Firefox(executable_path="./geckodriver")
    driver.get("https://kyfw.12306.cn/otn/resources/login.html")
    driver.maximize_window()
    sleep(1)
    driver.find_element_by_class_name('login-hd-account').click()
    sleep(2)

    driver.save_screenshot('bg.png')

    # we need to find the area of verification code image
    code_img_ele = driver.find_element_by_xpath('//*[@id="J-loginImg"]')
    # code image left-top coordinate
    location = code_img_ele.location
    # code image size x offset & y offset
    size = code_img_ele.size

    # code image left-top & right-bottom coordinates
    cutRange = (
        2*int(location['x']), 2*int(location['y']),
        2*int(location['x'] + size['width']), 2*int(location['y'] + size['height'])
    )

    # cut the image
    code_image_ptr = Image.open('./bg.png')
    code_image_name = 'code.png'
    frame = code_image_ptr.crop(cutRange)
    frame.save(code_image_name)

    # give the code image to workers to identify
    chaojiying = Chaojiying_Client('chaojiyingID', 'password', '912365')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('code.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    result = chaojiying.PostPic(im, 9004)['pic_str'] # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加() 9004
    print(result)
    # coordinates of points that will be clicked
    all_list = []

    if '|' in result:
        list_1 = result.split('|')
        count_1 = len(list_1)
        for i in range(count_1):
            xy_list = []
            x = int(list_1[i].split(',')[0])
            y = int(list_1[i].split(',')[1])
            xy_list.append(x)
            xy_list.append(y)
            all_list.append(xy_list)
    else:
        x = int(result.split(',')[0])
        y = int(result.split(',')[1])
        xy_list = []
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)

    print(all_list)
    for l in all_list:
        x = l[0] / 2
        y = l[1] / 2
        ActionChains(driver).move_to_element_with_offset(code_img_ele, x, y).click().perform()
        sleep(1)

    driver.find_element_by_id('J-userName').send_keys('Id')
    sleep(1)
    driver.find_element_by_id('J-password').send_keys('password')
    sleep(5)
    driver.find_element_by_id('J-login').click()
    sleep(10)
    driver.quit()
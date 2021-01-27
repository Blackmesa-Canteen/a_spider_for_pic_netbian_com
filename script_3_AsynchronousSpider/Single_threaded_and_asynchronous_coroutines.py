# -*- coding:utf-8 -*-
# @FileName  :Single_threaded_and_asynchronous_coroutines.py
# @Time      :2021/1/27 11:08 AM
# @Author    :Xiaotian

import asyncio
import time
import requests


async def request(url):
    print('requesting ' + url)
    # we can't use synchronized function in asynchronised functions
    # time.sleep(2)
    await asyncio.sleep(2)
    print('requesting successed', url)

urls = [
    'https://996.icu/',
    'https://www.996wokers.icu/',
    'https://www.working996.icu'
]

if __name__ == '__main__':
    # the function followed by async, need to return an object
    c = request('www.baidu.com')

    # create a loop of events
    # loop = asyncio.get_event_loop()


    # register objects in loop
    # loop.run_until_complete(c)

    # we can also create task objects
    # task = loop.create_task(c)
    # print(task)
    # loop.run_until_complete(task)
    # print(task)

    # using future. Diff: whether task is based on loop or not
    # task = asyncio.ensure_future(c)
    # print(task)
    # loop.run_until_complete(task)
    # print(task)

    # binding call-back functions

    # multiple tasks
    task_list = []
    start_time = time.time()
    for url in urls:
        c = request(url)
        task = asyncio.ensure_future(c)
        task_list.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))
    print(time.time() - start_time)

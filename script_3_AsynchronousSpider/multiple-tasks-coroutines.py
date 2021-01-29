# -*- coding:utf-8 -*-
# @FileName  :multiple-tasks-coroutines.py
# @Time      :2021/1/29 12:52 AM
# @Author    :Xiaotian

import asyncio
import time
# import aiohttp

async def request(url):
    print("downloading", url)

    #  if using requests.get(), using aiohttp package!
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(url) as response:
    #         page_text = await response.text()
    #        # content? no! using read() !
    #        # json?  using json() !
    await asyncio.sleep(2)

    print('done')

urls = [
    'https://www.baidu.com/',
    'https://www.sogou.com/',
    'https://www.163.com/'
]

task_list = []
if __name__ == '__main__':
    start = time.time()
    for url in urls:
        c = request(url)
        task = asyncio.ensure_future(c)
        task_list.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))

    print(-start + time.time())
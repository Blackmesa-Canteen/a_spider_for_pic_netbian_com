# -*- coding:utf-8 -*-
# @FileName  :single_thread_demo.py
# @Time      :2021/1/26 11:51 PM
# @Author    :Xiaotian
import requests
import time
from multiprocessing.dummy import Pool
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
    }

urls = [
    'https://www.baidu.com/',
    'https://www.sogou.com/',
    'https://www.163.com/'
]

def get_content(url):
    print('working...', url)
    response  = requests.get(url=url, headers=headers)
    time.sleep(2)
    if response.status_code == 200:
        return response.content

def parse_content(content):
    print('response\'s length is', len(content))

if __name__ == '__main__':
    start_time = time.time()
    # for url in urls:
    #    content =  get_content(url)
    #    parse_content(content)

    # Instantiate a thread pool
    thePool = Pool(3)
    thePool.map(get_content, urls)

    end_time = time.time()

    print('%d second' % (end_time - start_time))
    thePool.close()
    thePool.join()
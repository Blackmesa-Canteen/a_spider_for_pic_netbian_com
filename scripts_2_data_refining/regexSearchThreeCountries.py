import requests
from bs4 import BeautifulSoup
import time
import random
import lxml
if __name__ == '__main__':
    indexUrl = "https://www.shicimingju.com/book/sanguoyanyi.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    page_content = requests.get(url=indexUrl, headers=headers).content
    page_text = str(page_content,'utf-8')

    # print(page_text)

    # instantiate BeautifulSoup object
    soup = BeautifulSoup(page_text, 'lxml')

    # get title
    li_list = soup.select('.book-mulu > ul > li')
    # print(li_list)

    fp = open('../texts/sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        time.sleep(random.randint(2, 4))
        title = li.a.string
        detail_url = 'https://www.shicimingju.com' +\
            li.a['href']

        detail_content = requests.get(url=detail_url, headers=headers).content
        detail_text = str(detail_content, 'utf-8')

        # detail_text = requests.get(url=detail_url, headers=headers).text

        detail_soup = BeautifulSoup(detail_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        content = div_tag.text
        fp.write(title + ': ' + content + '\n')
        print(title, "successed")



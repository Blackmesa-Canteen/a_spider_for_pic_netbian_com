import requests

if __name__ == '__main__':
    # url
    url = 'https://www.sogou.com/'

    # request
    response = requests.get(url=url)

    page_text = response.text


    with open('../htmls/ssogasou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print('done')
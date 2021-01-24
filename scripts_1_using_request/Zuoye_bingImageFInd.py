import requests

if __name__ == '__main__':
    url = "https://cn.bing.com/images/search"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
    }

    params = {
        'q': 'saber',
        'go': 'Search',
        'qs': 'ds',
        'form': 'QBIR'
    }

    response = requests.get(url=url, params=params, headers=headers)

    res_text = response.text

    with open('../htmls/saberImageResult.html', 'w', encoding='utf-8') as fp:
        fp.write(res_text)

    print('done')
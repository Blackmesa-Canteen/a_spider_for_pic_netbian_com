import requests
import json

if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list"
    param = {
        'type': '17',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
    }

    response = requests.get(url=url, params=param, headers=headers)

    res_list = response.json()

    fp = open('../jsons/doubanMovie.json', 'w', encoding='utf-8')
    json.dump(res_list, fp=fp, ensure_ascii=False)
    print("done")



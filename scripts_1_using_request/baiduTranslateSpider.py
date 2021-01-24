import requests
import json

if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
    keyword = input("translate what:")
    data = {
        'kw': keyword
    }

    headers = {
        'User-Agent': user_agent
    }

    response = requests.post(url=post_url, data=data, headers=headers)
    # if you are sure that
    # the response type is json
    res_obj = response.json()

    fp = open('../jsons/' + keyword + '.json', 'w', encoding='utf-8')
    json.dump(res_obj, fp=fp, ensure_ascii=False)

    print('done')

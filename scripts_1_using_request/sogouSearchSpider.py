import requests

# UA disguise
if __name__ == '__main__':

    url = "https://www.sogou.com/web"
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'

    # handle parameters in url
    keyword = input("请输入搜索关键词： ")

    header_dict = {
        'User-Agent': user_agent
    }

    param_dict = {
        'query': keyword
    }

    # send get request
    response = requests.get(url=url, params=param_dict, headers=header_dict)

    page_text = response.text

    fileName = '../htmls/' + keyword + '_result.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, 'saved')

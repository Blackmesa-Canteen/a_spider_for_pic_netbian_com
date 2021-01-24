import requests
import json

if __name__ == '__main__':
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
    }

    # example: 粤妆20210024
    # Id = "粤妆20210024"
    Id = input("想找许可证信息，按许可证编号查询一下吧： ")
    query_data = {
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName': Id,
        'conditionType': '1',
        'applyname': '',
        'applysn': ''
    }

    response = requests.post(url,
                             headers=headers,
                             data=query_data)
    json_dict = response.json()
    res_list = json_dict['list']

    res = ''
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    for dict in res_list:
        if dict is None:
            print("not found")
            break
        else:
            certificateId = dict['ID']

            query_data = {
                'id': certificateId
            }
            response = requests.post(url, data=query_data, headers=headers)
            json_dict = response.json()

            res += '证名儿:' + Id + '\n' + \
                  '法人名儿:' + json_dict['businessPerson'] + '\n' + \
                  '公司名儿:' + json_dict['epsName'] + '\n' + \
                  '公司地址儿:' + json_dict['epsAddress'] + '\n' + \
                  '做啥子:' + json_dict['certStr'] + '\n\n'


    print('\n' + res)
    with open('../texts/HuaZhuangRes.txt', 'w', encoding='utf-8') as fp:
        fp.write(res)
    print("ok")

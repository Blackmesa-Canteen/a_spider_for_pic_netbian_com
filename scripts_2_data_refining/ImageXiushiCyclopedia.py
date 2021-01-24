import requests
if __name__ == '__main__':
    url = "https://pic.qiushibaike.com/system/pictures/12400/124002579/medium/7PUDF5G741LEV8TO.jpg"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
    }

    # text: returns string
    # content: returns bin
    # json(): returns object
    image_bin_data = requests.get(url=url, headers=headers).content

    with open('../images/xiutuImage.jpg', 'wb') as fp:
        fp.write(image_bin_data)

    print('done')

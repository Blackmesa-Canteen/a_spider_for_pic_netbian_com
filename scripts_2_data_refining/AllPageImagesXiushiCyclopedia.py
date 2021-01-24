import requests
import re
import os

if __name__ == '__main__':
    # template url
    urlTemplate = "https://www.qiushibaike.com/imgrank/page/%d/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    # make a folder to store images
    if not os.path.exists('../qiutuImages'):
        os.mkdir('../qiutuImages')

    # change pages
    for pageNum in range(1, 3):
        url = format(urlTemplate % pageNum)
        # use universal spider to retrieve html
        page_sc = requests.get(url=url, headers=headers).text
        # use focus spider to retrieve all images from that html

        # note:
        # <div class="thumb">
        # <a href="/article/123920552" target="_blank">
        # <img src="//pic.qiushibaike.com/system/pictures/12392/123920552/medium/3KMBS7Z5BXOQS4KY.jpg" alt="糗事#123920552" class="illustration" width="100%" height="auto">
        # </a>
        # </div>
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex, page_sc, re.S)
        # print(img_src_list)

        for img_origin_src in img_src_list:
            img_src = 'https:' + img_origin_src
            # got the image binary content
            img_bin = requests.get(img_src, headers=headers).content

            # generate name
            img_name = img_src.split('/')[-1]
            imgPath = '../qiutuImages/' + img_name + '.jpg'
            with open(imgPath, 'wb') as fp:
                fp.write(img_bin)
                print(img_name + ' downloaded')

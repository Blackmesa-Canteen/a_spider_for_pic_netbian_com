# -*- coding:utf-8 -*-
from lxml import etree

if __name__ == '__main__':
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse('../htmls/sogou.html', parser=parser)
    r = tree.xpath('/html/head//text()')
    print(r)

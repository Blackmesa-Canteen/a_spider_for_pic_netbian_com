from bs4 import BeautifulSoup

if __name__ == '__main__':
    fp = open('../htmls/sogou.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')

    # print(soup.div) # soup.tagName returns first element that occurs in html
    # print(soup.find('div'))
    # print(soup.select('.header')) # returns a list
    print(soup.select('a')[0]['href'])
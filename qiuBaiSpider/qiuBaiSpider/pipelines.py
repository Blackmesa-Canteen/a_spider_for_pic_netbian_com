# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql as pymysql
from itemadapter import ItemAdapter


class QiubaispiderPipeline(object):
    fp = None
    def open_spider(self):
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')
    # used to handle Item objects
    # every time it yields a item, it will work for once
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        self.fp.write(author + ': ' + content + '\n')

        return item

    def close_spider(self):
        self.fp.close()

class MysqlPipeLine(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='', db='unichat', charset='utf8')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute('INSERT INTO unichat.qiubai (name, content) VALUES ("%s", "%s") ' % (item["author"], item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
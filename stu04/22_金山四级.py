#coding:utf-8
# @Time  : 2021/2/23 13:57
# @Author: Netfj@sina.com
# @File  : 21.py
# @info  : 爬取金山四级词汇的示例

from urllib import request
from lxml import etree

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

# 词汇表
words = []
fo = open("word.txt", "w",encoding = 'utf-8')


def shanbei():
    url = "https://www.eol.cn/html/en/cetwords/cet4.shtml"
    print(url)

    fo.write(url + '\n--------------------------------------------------------\n')

    rsp = request.urlopen(url)

    html = rsp.read()

    # 解析html
    html = etree.HTML(html)
    html_data = html.xpath('//p/text()')

    n=1
    for i in html_data:
        print(n,i)
        n += 1
        fo.write(i + "\n\n")


def create_database():
    sys.path.append(r"..\suport")
    from SQLiteClass import Dbt,log_config

    log_config()

    db = Dbt()

    db.database_connect("dict.sqlite")
    db.table_create('words', ['ID Integer PRIMARY KEY autoincrement',
                              'word varchar(30) not null',
                              'type varchar(10) not null',
                              'meanings text nou null ' ])
    db.value_insert('words',"('id','word','type','meanings')","(33,'Tom','n.','汤姆')")

    re = db.query_table("words")
    print(re)
    db.database_disconnect()


if __name__ == '__main__':
    shanbei()
    # create_database()
#coding:utf-8
# @Time  : 2021/2/23 13:57
# @Author: Netfj@sina.com
# @File  : 21.py
# @info  : 

from urllib import request
from lxml import etree

# 词汇表
words = []
fo = open("word.txt", "w")


def shanbei(page):
    url = "https://www.shanbay.com/wordlist/104899/202159/?page=%s" % page
    print(url)

    fo.write(url + '\n--------------------------------------------------------\n')

    rsp = request.urlopen(url)

    html = rsp.read()

    # 解析html
    html = etree.HTML(html)

    tr_list = html.xpath("//tr")

    # 遍历每个tr元素，每一个tr对应一个单词和介绍
    for tr in tr_list:
        word = {}
        strong = tr.xpath('.//strong')
        str = tr.xpath('.//td')


        if len(strong):
            # strip把找到的内容去掉空格
            name = strong[0].text.strip()
            str = str[1].text.strip()

            word['name'] = name
            word['str'] = str
            print(word)

            fo.write(name + "\n" + str +"\n\n")


if __name__ == '__main__':
    page = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for x in page:
        shanbei(x)
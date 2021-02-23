#coding:utf-8
# @Time  : 2021/2/23 16:09
# @Author: Netfj@sina.com
# @File  : 23.py
# @info  : 

from urllib import request
from bs4 import BeautifulSoup
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

url = "https://www.eol.cn/html/en/cetwords/cet4.shtml"
rsp = request.urlopen(url)
html = rsp.read()

soup = BeautifulSoup(html,'lxml')
tags = soup.find_all(attrs = {'class':'wordL fl'})
for tag in tags:
    p_list = tag.select('p')
    for p in p_list:
        print(p)
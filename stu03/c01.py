#coding:utf-8
"""
Info:
@author:Netfj@sina.com  @software: PyCharm @file: 01.py @time: 2018/11/3 16:58
"""

import tkinter
top = tkinter.Tk()
# 进入消息循环
top.mainloop()

root = tkinter.Tk()  # 创建窗口对象的背景色
# 创建两个列表
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb = tkinter.Listbox(root)  # 创建两个列表组件
listb2 = tkinter.Listbox(root)
for item in li:  # 第一个小部件插入数据
    listb.insert(0, item)

for item in movie:  # 第二个小部件插入数据
    listb2.insert(0, item)

listb.pack()  # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()  # 进入消息循环
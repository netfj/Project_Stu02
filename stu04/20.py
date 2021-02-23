#coding:utf-8
# @Time  : 2021/2/23 15:06
# @Author: Netfj@sina.com
# @File  : 20.py
# @info  : 


from lxml import etree

wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">【1】first item</a></li>
                 <li class="item-1"><a href="link2.html">【2】second item</a></li>
                 <li class="item-inactive"><a href="link3.html">【3】third item</a></li>
                 <li class="item-1"><a href="link4.html">【4】fourth item</a></li>
                 <li class="item-0"><a href="link5.html">【5】fifth item</a>
             </ul>
         </div>
         <p>test</p>
        """

print('\n生成 HTML 文件对象，即：从网站请求的网页文件格式')
html = etree.HTML(wb_data)
print(html)

print('\n转化为字符串')
result = etree.tostring(html)
print(result.decode("utf-8"))

print('\n获取 <a> 标签中的数据 之 方法1')
html_data = html.xpath('/html/body/div/ul/li/a')
for i in html_data:
    print(i.text)


print('\n获取 <a> 标签中的数据 之 方法2: 直接在需要查找内容的标签后面加一个/text()就行')
html_data = html.xpath('/html/body/div/ul/li/a/text()')
for i in html_data:
    print(i)



print('\n使用 parse 打开 html 文件')
html_data = html.xpath('//*')   #打印是一个列表，需要遍历
for i in html_data:
    print(i.text)

print('\n打印指定路径下a标签的属性（可以通过遍历拿到某个属性的值，查找标签的内容）')
html_data = html.xpath('/html/body/div/ul/li/a/@href')
for i in html_data:
    print(i)

print('\n查找绝对路径下a标签属性等于link2.html的内容。')
html_data = html.xpath('/html/body/div/ul/li/a[@href="link2.html"]/text()')
print(html_data)
for i in html_data:
    print(i)

print('\n上面我们找到全部都是绝对路径（每一个都是从根开始查找），下面我们查找相对路径，例如，查找所有li标签下的a标签内容。')
html_data = html.xpath('//li/a/text()')
print(html_data)
for i in html_data:
    print(i)

print('上面我们使用绝对路径，查找了所有a标签的属性等于href属性值，利用的是/---绝对路径，下面我们使用相对路径，查找一下l相对路径下li标签下的a标签下的href属性的值，注意，a标签后面需要双//。')
html = etree.HTML(wb_data)
html_data = html.xpath('//li/a//@href')
print(html_data)
for i in html_data:
    print(i)


print('相对路径下跟绝对路径下查特定属性的方法类似，也可以说相同。')
html_data = html.xpath('//li/a[@href="link2.html"]')
print(html_data)
for i in html_data:
    print(i.text)

print('查找最后一个li标签里的a标签的href属性')
html_data = html.xpath('//li[last()]/a/text()')
print(html_data)
for i in html_data:
    print(i)


print('查找倒数第二个li标签里的a标签的href属性')
html_data = html.xpath('//li[last()-1]/a/text()')
print(html_data)
for i in html_data:
    print(i)



# 如果在提取某个页面的某个标签的xpath路径的话，可以如下图：
#
# 　　//*[@id="kw"]
#
# 　　解释：使用相对路径查找所有的标签，属性id等于kw的标签。




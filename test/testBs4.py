#-*- coding = utf-8 -*-
#@Time ： 2020/4/17 19:56
#@Author : Alworm
#@File : testBs4.py
#@Software : PyCharm

from bs4 import BeautifulSoup
import urllib.request
'''
response = urllib.request.urlopen("http://www.baidu.com")
html = response.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")
print(type(bs))
print(bs.title)
print(bs.title.string)
'''
#文档遍历
'''
print(len(bs.head.contents))
print(bs.head.contents)
print()
print(bs.head.contents[1])
'''
#文档搜索
#1.find_all()
'''
response = urllib.request.urlopen("http://www.baidu.com")
html = response.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")
t_list = bs.find_all('a')
for i in range(len(t_list)):
    print(t_list[i])
'''

#正则表达式搜索
'''
import re
response = urllib.request.urlopen("http://www.baidu.com")
html = response.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")
t_list = bs.find_all(re.compile("a"))
print(t_list)
'''
#通过函数，根据函数查找
'''
def name_is_exists(tag):
    return tag.has_attr("name")
response = urllib.request.urlopen("http://www.baidu.com")
html = response.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")
t_list = bs.find_all(name_is_exists)
print(t_list)
'''
#根据属性，类查找
import re
response = urllib.request.urlopen("http://www.baidu.com")
html = response.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")
'''
t_list = bs.find_all(id="head")
for item in t_list:
    print(item)

t_list2 = bs.find_all(class_=True)
print("*"*30)
for item in t_list2:
    print(item)

t_list3 = bs.find_all(text="地图")
t_list4 = bs.find_all(text={"地图", "hao123"})
print(t_list4)
print("*"*100)
t_list5 = bs.find_all(text=re.compile("\d"))
for item in t_list5:
    print(item)
'''

#limit
'''
t_list = bs.find_all("a",limit=3)
for item in t_list:
    print(item)
'''

#选择器
#类名
'''
t_list = bs.select(".mnav")
for item in t_list:
    print(item)
'''
#通过id
'''
t_list = bs.select("#u1")
for item in t_list:
    print(item)
'''
'''
t_list = bs.select("a[class='pf']")
for item in t_list:
    print(item)
# <a class="pf" href="javascript:;" name="tj_settingicon">设置<i class="c-icon c-icon-triangle-down"></i></a>
# <a class="pf" href="http://www.baidu.com/gaoji/preferences.html" name="tj_settingicon">设置</a>
'''
#子标签
'''
t_list = bs.select("head > title")
for item in t_list:
    print(item)
'''
#兄弟标签
'''
t_list = bs.select(".mnav ~ .pf")
print(t_list[0].get_text())
'''
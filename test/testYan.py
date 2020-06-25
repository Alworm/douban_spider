# -*- coding = utf-8 -*-
# @Time ： 2020/4/21 14:28
# @Author : Alworm
# @File : testYan.py
# @Software : PyCharm

from bs4 import BeautifulSoup#网页解析
import re  #政策表达式
import urllib.request,urllib.error #制定url，获取网页数据
import xlwt #excel操作

url = "http://202.194.116.70/meol/jpk/course/layout/newpage/index.jsp?courseId=14017"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
        "Cookie": "JSESSIONID=DC57D0B18CAE335F87BF1C0FB94CBB7E.TM1; DWRSESSIONID=PHAxB9CWcXZlb3aq15GDHcFlr7n"
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

html = response.read().decode("GBK")
print(html)
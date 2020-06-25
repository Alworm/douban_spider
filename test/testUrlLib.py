#-*- coding = utf-8 -*-
#@Time ： 2020/4/17 8:33
#@Author : Alworm
#@File : testUrlLib.py
#@Software : PyCharm

import urllib.request
'''
#reqeust in 'get' way
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode("utf-8")) #utf-8解码 encode 编码
'''
'''
#request in 'post' way
import urllib.parse
data = bytes(urllib.parse.urlencode({"Alworm":"Alworm"}),encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post",data = data)
print(response.read().decode("utf-8"))
'''

'''
#超时处理
try:
    response = urllib.request.urlopen("http://www.baidu.com",timeout=1)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out")
'''
import urllib.parse
# url = "http://httpbin.org/post"
url = "https://www.douban.com"
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
data = bytes(urllib.parse.urlencode({"Alworm":"Alworm"}),encoding="utf-8")
request = urllib.request.Request(url, headers=headers, data=data, method="POST")
response = urllib.request.urlopen(request)
print(response.read().decode("utf-8"))



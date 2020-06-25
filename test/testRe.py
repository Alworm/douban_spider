#-*- coding = utf-8 -*-
#@Time ： 2020/4/19 14:55
#@Author : Alworm
#@File : testRe.py
#@Software : PyCharm

import re
#1.0先创新模式对象
'''
pat = re.compile("AA") #是正则表达式
m = pat.search("CBA")
m2 = pat.search("ABACAA")
print(m)#None
print(m2)#<re.Match object; span=(4, 6), match='AA'>
'''
#2.0没有创建模式对象
'''
m = re.search("abc","Aabc")
print(m)
'''
#findall
'''
print(re.findall("[A-Z]", "ABCDabcdEFGDgfg"))#['A', 'B', 'C', 'D', 'E', 'F', 'G', 'D']

print(re.findall("[A-Z]+", "ABCDabcdEFGDgfg"))
'''
#sub
'''
print(re.sub("a", "A", "abcdDCabc")) #替换
'''


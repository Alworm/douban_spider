# -*- coding = utf-8 -*-
# @Time ： 2020/4/20 14:25
# @Author : Alworm
# @File : testXlmt.py
# @Software : PyCharm

import xlwt
'''
workbook = xlwt.Workbook(encoding="utf-8")      # 创建workbook对象
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0, 0, 'hello')
workbook.save("student.xls")
'''
workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('sheet1')
for i in range(1, 10):
    for j in range(1, i+1):
        worksheet.write(i-1, j-1, str(i)+'*'+str(j)+'='+str(i*j))
workbook.save("mul.xls")



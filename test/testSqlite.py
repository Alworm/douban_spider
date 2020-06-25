# -*- coding = utf-8 -*-
# @Time ： 2020/4/20 15:29
# @Author : Alwormtest.db
# @File : testSqlite.py
# @Software : PyCharm

import sqlite3

sql = '''
    create table company
    (id int primary key not null,
    name text not null,
    age int not null,
    address char(50),
    salary real);
'''
# 创建数据库
'''
conn = sqlite3.connect("test.db")
print("Opened database successfully")
c = conn.cursor()
'''
# 创建表
'''
c.execute(sql)
conn.commit()
conn.close()
print("成功建表")
'''


# 插入数据
sql2 = '''
    insert into company(id,name,age,address,salary)
    values (3,"lisi",32,"成都", 8000);
'''

'''
conn = sqlite3.connect("test.db")
print("Opened database successfully")
c = conn.cursor()
c.execute(sql2)
conn.commit()
conn.close()
'''

# 查询数据
sql3 = '''
    select * from company;
'''
conn = sqlite3.connect("test.db")
print("Opened database successfully")
c = conn.cursor()
cursor = c.execute(sql3)
for row in cursor:
    print("id=", row[0])
    print("name=", row[1])
    print("address=", row[2])
    print("salary=", row[3], "\n")
conn.commit()
conn.close()
# -*- coding = utf-8 -*-
# @Time ： 2020/4/17 8:09
# @Author : Alworm
# @File : spider.py
# @Software : PyCharm

from bs4 import BeautifulSoup#网页解析
import re  #政策表达式
import urllib.request,urllib.error #制定url，获取网页数据
import xlwt #excel操作
import sqlite3

# 影片的链接
findLink = re.compile(r'<a href="(.*?)">')
# 影片的图片
findImgSrc = re.compile(r'<img alt=".*" src="(.*?)"', re.S)     # .是不包括换行符的，在这里re.S让换行符包含其中
# 影片的主题
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片的评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 得到指定一个URL的网页内容
def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
        print("html获取成功")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 获取网页数据
def getData(baseurl):
    datalist = []
    for i in range(10):
        url = baseurl+str(i*25)
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            data = []                                   # save the movie's informaiton
            item = str(item)
            # print(item)
            link = re.findall(findLink, item)[0]
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)        # 片名可能有多个名字，也可能只有一个中文名字
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")                        # 没有外国名字要留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)                         # 添加评分

            judge = re.findall(findJudge, item)[0]
            data.append(judge)                          # 评价人数

            inq = re.findall(findInq, item)             # 添加描述
            if len(inq) !=0:
                inq = inq[0].replace(".", "")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>', " ", bd)          # 去掉<br/>
            bd = re.sub('/', " ", bd)                    # 替换/
            data.append(bd.strip())                     # 去掉前后的空格

            datalist.append(data)

    # for index, item in enumerate(datalist):
    #     print("%d\n:%s" % (index, item))
    return datalist


# 保存爬取的数据到excel
def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "影片中文名称", "影片外文名称", "评分", "平分数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i+1, j, data[j])
    book.save(savepath)


def init_db(dbpath):
    sql = '''
        create table if not exists movie250
        (
            id integer primary key autoincrement,
            info_link text,
            pick_link text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            introduction text,
            info text
        );
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()



# 保存爬取的数据到数据库
def saveDataToDb(datalist, savepath):
    init_db(savepath)
    conn = sqlite3.connect(savepath)
    cursor = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movie250(
                info_link, pick_link, cname, ename, score, rated, introduction, info)
                values (%s)''' % ",".join(data)
        # print(sql)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


def main():
    print("开始爬取！")
    baseurl = "https://movie.douban.com/top250?start="
    dbpath = "movie.db"
    # savepath = ".\\电影豆瓣Top250(2).xls"

    # 1.获取网页数据
    datalist = getData(baseurl)
    '''
    for index, item in enumerate(datalist):
        print("*%d*\n:%s\n"%(index, item))
    '''
    # 2.1保存数据到数据库
    saveDataToDb(datalist, dbpath)

    # 2.2保存数据到excel
    # saveData(datalist, savepath)

    print("爬取结束！")


if __name__ == "__main__":
    main()
    # init_db('movietest.db')
    print("done!")

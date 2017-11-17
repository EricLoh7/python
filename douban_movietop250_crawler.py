# !/usr/bin/env python
# -*- coding:utf-8 -*-

import lxml,requests,re,time
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://movie.douban.com/top250"
filename = "豆瓣TOP250.xlsx"
wb = Workbook()
ws1 = wb.active
ws1.title ="豆瓣top250"
data = []
info = ["电影","评分","人数","短评"]
ws1.append(info)

def download_url():
    #解析url
    proxies = {'https': 'http://61.160.208.222:8080'}
    downloadurl = url
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}

    def update_url():
        while True:
            try:
                next_url = soup.find("span", attrs={"class": "next"}).find("link")["href"]
                downloadurl = url + next_url
                return downloadurl
            except Exception as err:
                pass
    page = 1
    while True:
        print("正在读取第%s页......"%(page))
        page += 1
        html = requests.get(downloadurl,headers=headers,proxies = proxies).content
        soup = BeautifulSoup(html,"lxml")

        # 依次获取电影名字，电影评分，电影评价人数，电影短评
        movie_all_detail = soup.find("ol",attrs = {"class":"grid_view"})
        for movie_detail in movie_all_detail.find_all("li"):
            temp_list = []
            movie_name = movie_detail.find("div",attrs ={"class":"hd"}).find("span",attrs = {"class":"title"}).string
            temp_list.append(movie_name)

            movie_score =movie_detail.find("div",attrs = {"class":"star"}).find("span",attrs = {"class":"rating_num"}).string
            temp_list.append(movie_score)

            str= movie_detail.find("div",attrs = {"class":"star"})
            movie_score_people = str.find(text=re.compile("评价"))
            temp_list.append(movie_score_people.strip("人评价"))

            try:
                short_comment = movie_detail.find("p",attrs ={"class":"quote"}).find("span",{"class":"inq"}).string
                temp_list.append(short_comment)
                data.append(temp_list)
            except Exception as e:
                pass
            ws1.append(temp_list)

        downloadurl = update_url()
        if not downloadurl:
            wb.save(filename)
            break
        else:
            time.sleep(2)

download_url()
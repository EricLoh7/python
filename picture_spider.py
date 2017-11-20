# !/usr/bin/env python
# -*- coding:utf-8 -*-

import requests,os,lxml
from bs4 import BeautifulSoup

class Pic_Download():

    def __init__(self,number_of_page):
        header ={"referer":"https://girl-atlas.com/album/5885e90692d3027f35837164","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
        self.session = requests.Session()
        self.session.headers.update(header)
        self.number_of_page = number_of_page

    def get_url(self):
        os.mkdir(r"C:\Users\Administrator\Desktop\picture")
        page = 1
        while True:
            print("正在下载第%s页......"%str(page))
            url ="https://girl-atlas.com/?p=%s"%(str(page))
            html = self.session.get(url)
            soup = BeautifulSoup(html.content,"lxml")
            all_girls = soup.find_all("div",attrs = {"class":"album-item row"})
            for girl in all_girls:
                girl_detail = girl.find("div", attrs = {"class":"col-md-11 col-sm-11"})
                girl_url = girl_detail.find("h2").a["href"]
                file_name = girl_detail.find("h2").string
                try:
                    os.mkdir(r"C:\Users\Administrator\Desktop\picture\%s"%(file_name))
                except Exception as e:
                    os.mkdir(r"C:\Users\Administrator\Desktop\picture\%s"%(file_name+str(page)))
                new_url = "https://girl-atlas.com"+girl_url
                html = self.session.get(new_url)
                soup = BeautifulSoup(html.content,"lxml")
                all_picture = soup.find("ul",attrs ={"class":"slideview"}).find_all("li",attrs = {"class":"slide"})
                number = 1
                for picture in all_picture:
                    try:
                        download_url = picture.img["src"]
                    except Exception as e:
                        download_url = picture.img["delay"]
                    with open (r"C:\Users\Administrator\Desktop\picture\%s\%s"%(file_name.strip(),str(number)+".jpg"),"wb") as f:
                        f.write(self.session.get(download_url).content)
                        number += 1
            if  self.number_of_page - page > 0:
                print("第%s页已经下载完成，还剩%s页....请稍等..." %(str(page),str(self.number_of_page - page)))
            else:
                print("所有文件已经下载完成")
            if page < self.number_of_page:
                page += 1
            else:
                break



if __name__ == "__main__":
    ll =Pic_Download(20)
    ll.get_url()
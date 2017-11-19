# !/usr/bin/env python
# -*- coding:utf-8 -*-

import requests,lxml,pprint
from bs4 import BeautifulSoup

class Get_Free_Proxies():
    def __init__(self,ip_anonymous = "高匿",ip_type = "HTTP",url = "http://www.xicidaili.com/"):
        self.ip_type = ip_type
        self.ip_anonymous = ip_anonymous
        self.url = url

    def download_html(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"}
        html = requests.get(self.url,headers = headers)
        print(html.status_code)
        self.soup = BeautifulSoup(html.content,"lxml")

    def html_parser(self):
        self.ip_list = []
        self.download_html()
        tem_ip_list = self.soup.find("table",attrs = {"id":"ip_list"})
        ip_all = tem_ip_list.find_all("tr")
        for ip_detail in ip_all:
            try:
                ip_info = ip_detail.find_all("td")
                ip = ip_info[1].string+":"+ip_info[2].string
                ip_addr = ip_info[3].string
                ip_anony = ip_info[4].string
                ip_tp = ip_info[5].string
                self.ip_list.append([ip,ip_addr,ip_anony,ip_tp])
            except Exception as e:
                pass
    def print_ip(self):
        self.html_parser()
        for i in self.ip_list:
            if i[3] == self.ip_type and i[2] == self.ip_anonymous:
                print(i)
    def print_all_ip(self):
        pprint.pprint(self.ip_list)


foo = Get_Free_Proxies("透明","HTTPS")
foo.print_ip()
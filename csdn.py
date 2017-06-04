# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:26:06 2017

@author: zch
"""
#爬取页面链接
import re
import urllib.request

def getlink(url):
    #模拟浏览器
    headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    #根据需要构建链接表达式
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    #去除重复元素
    link = list(set(link))
    return link

#要爬取的网页链接
url = "http://blog.csdn.net/"
#获取对应网页中包含的链接地址
linklist = getlink(url)
#通过for循环分别遍历输出获取的链接地址
for link in linklist:
    print(link[0])



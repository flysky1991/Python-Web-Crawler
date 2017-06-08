# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:24:27 2017

@author: zch
"""

import re
import urllib.request

def craw(url,page):
    #获取网页源代码
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    #对网页源码进行过滤，只保留和产品列表相关的信息
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    #print(result1)
    #再次过滤，提取网页中图片的链接，并将链接地址存储在列表中
    pat2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imagelist = re.compile(pat2).findall(result1)
    x = 1
    #遍历列表，将链接存储到本地
    for imageurl in imagelist:
        imagename = "E:/Python/data/jd/phone/" + str(page) + str(x) + ".jpg"
        imageurl = "http://" + imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1
#通过for循环，将该分类下的所有网页都爬取一遍
for i in range(1,66):
    print("Downloading page " + str(i) + "...")
    url = "https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    craw(url,i)

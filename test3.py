# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:44:30 2017

@author: Administrator
"""

import re
import urllib.request
from bs4 import BeautifulSoup


def crawl(url,page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    #对网页源代码进行初步过滤
    pat1 = '<ul class="util-clearfix son-list">.+?</ul>'
    #pat1 = "//li"
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    #print(result1)
    
    """
    要在两者之间加一个循环逻辑,未完待续...
    """
    #筛选出result1中包含<div class="pic">的标签信息
    pat2 = '<div class="pic">.+?</div>'
    #pat2 = '<li pub-catid="200000347">.+?</li>'
    result2 = re.compile(pat2).findall(result1)
    result2 = result2[0]
    #print(result2)
    
    #进一步提取出商品名和商品图片信息
    soup1 = BeautifulSoup(result2,'lxml') 
    #print(soup.prettify())
    result21 = soup1.find('img')
    #print(result3)
    
    purl = result21['src']
    ptitle = result21['alt']
    print("第一个商品名为:"+ ptitle)
    print("第一个商品图片链接为:" + purl)
    imagename = "D:/Python/data/aliexpress/test/" + ptitle + ".jpg"
    urllib.request.urlretrieve(purl,filename=imagename)

    
    #筛选出result1中包含<div class="has-sku-image">的标签信息
    pat3 = '<div class="has-sku-image">.+?</div>'
    result3 = re.compile(pat3).findall(result1)
    result3 = result3[0]
    #print(result3)
    
    soup2 = BeautifulSoup(result3,'lxml')
    #print(soup2.prettify())
    result31 = soup2.find('a')
    #print(result31)
    ptitle = result31['title']
    #pcolor = result31
    print("第一个商品的标题为:" + ptitle)
    print("第一个商品可选的颜色有:" + result31.string)
    
    #筛选出result1中包含<div class="has-sku-image">的标签信息
    pat4 = '<span class="value">.+?</span>'
    result4 = re.compile(pat4).findall(result1)
    result4 = result4[0]
    print(result4)
    
    
    soup3 = BeautifulSoup(result4,'lxml')
    
    print("第一个商品的价格为:" + soup3.string)
    
    
    

    
    
    
for i in range(1,5):
    print("正在下载第%d页数据..." %i)
    #速卖通女装信息
    url = "file:///C:/Users/Administrator/Desktop/aliexpress/" + str(i) + ".html"
    crawl(url,i)
    
    

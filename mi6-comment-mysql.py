# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 9:18:38 2017

@author: Administrator
"""

import requests
import json
import time
import random
import pymysql.cursors


def crawlProductComment(url,page):
    req = requests.get(url)
    jsondata = req.text[15:]
    data = json.loads(jsondata)
    
    #输出页面信息
    print('page:',data['paginator']['page'])
    #遍历评论信息列表
    for i in data["rateList"]:
        #print(i)
        #输出商品sku信息
        auctionSku = i['auctionSku']
        print(auctionSku)
        #输出评论时间和评论内容
        rateDate = i['rateDate']
        rateContent = i['rateContent']
        print(rateDate,rateContent)
        info = i['appendComment']
        #判断是否有追加评论
        commentTime = ''
        content = ''
        if info:
            commentTime = info['commentTime']
            content = info['content']
            print(commentTime)
            print(content)
        print('=============================================')
        
        
        '''
        数据库操作
        '''
        
        #获取数据库链接
        connection  = pymysql.connect(host = 'localhost',
                                  user = 'root',
                                  password = '123456',
                                  db = 'tmall',
                                  charset = 'utf8mb4')
        try:
            #获取会话指针
            with connection.cursor() as cursor:
                #创建sql语句
                sql = "insert into `mi6` (`auctionSku`,`rateDate`,`rateContent`,`commentTime`,`content`) values (%s,%s,%s,%s,%s)"
                
                #执行sql语句
                cursor.execute(sql,(auctionSku,rateDate,rateContent,commentTime,content))
                
                #提交数据库
                connection.commit()
        finally:
            connection.close()
        

for i in range(2,21):
    print("正在获取第{}页评论数据!".format(i))
    #小米6评论链接
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=548997264334&spuId=109435847&spuId=109435847&sellerId=2024314280&order=3&currentPage=' + str(i) +'&append=⊙&content=1'
    crawlProductComment(url,i)
    #设置休眠时间
    time.sleep(random.randint(31,33))
    
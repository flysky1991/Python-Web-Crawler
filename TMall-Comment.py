# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 19:34:31 2017

@author: Administrator
"""

import requests
import json

#商品评论的JSON数据
url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=541396117031&spuId=128573071&spuId=128573071&sellerId=2616970884&order=3&currentPage=1&append=⊙&content=1'
req = requests.get(url)
jsondata = req.text[15:]
data = json.loads(jsondata)

#输出页面信息
print('page:',data['paginator']['page'])
#遍历评论信息列表
for i in data["rateList"]:
    #输出商品sku信息
    print(i['auctionSku'])
    #输出评论时间和评论内容
    print(i['rateDate'],i['rateContent'])
    info = i['appendComment']
    #判断是否有追加评论
    if info:
        print(info['commentTime'])
        print(info['content'])
    print('======')
#!/usr/bin/python3
# coding:utf-8

from tinydb import TinyDB, Query, where
from os import sys
import sys
import os
import os.path

p = os.path.abspath(__file__)
path = os.path.abspath(os.path.join(p, os.pardir))+'/db.json'
COMMAND = os.path.abspath(os.path.join(p, os.pardir))+'/_git_push.sh'

TinyDB.DEFAULT_TABLE = 'all'
db = TinyDB(path)


def AddItem(item):
    table = db.table('all')
    table.insert(item)
    print('Insert Item  Successed!!!')


def DeleteItem(id):
    db.table('all').remove(doc_ids=[id])
    print('Delete Item Successed !!!')
    # db.table('all').remove(doc_ids=[162])


# AddItem({
#     'describtion': 'Dev Ed',
#     'url': 'https://www.youtube.com/c/DevEd/videos',
#     "catalog": 'youtube'  # 小写
# })

# databases
# mongodb home page140


# table = db.table('all').update({'catalog': 'x'}, doc_ids=[
#     123, 143, 153, 154, 155, 158, 161])


# [Kindle电子书下载_在线阅读-Kindle电子书资源txt-亚马逊Kindle电子书官网](https://www.amazon.cn/Kindle%E7%94%B5%E5%AD%90%E4%B9%A6/b/461-2537587-0192803?ie=UTF8&node=116169071&ref_=nav_topnav_giftcert)

# db.table('all').update(
# {'describtion': '亚马逊Kindle电子书官网'}, doc_ids = [164])

# DeleteItem(145)


# os.system("sh COMMAND")
# os.system(COMMAND)

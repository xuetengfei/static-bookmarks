#!/usr/bin/python3
# coding:utf-8

from tinydb import TinyDB, Query, where
import os
import os.path

p = os.path.abspath(__file__)
path = os.path.abspath(os.path.join(p, os.pardir))+'/db.json'

TinyDB.DEFAULT_TABLE = 'all'
db = TinyDB(path)


def AddItem(item):
    table = db.table('all')
    table.insert(item)
    print('Insert Item  Successed!!!')


def DeleteItem(id):
    db.table('all').remove(doc_ids=[id])
    print('Delete Item Successed !!!')

# [冲浪普拉斯的个人空间_哔哩哔哩_Bilibili]()


goal = {
    'describtion': 'Developer Roadmaps',
    'url': 'https://roadmap.sh/',
    "catalog": 'dev'  # 小写
}


# AddItem(goal)

# DeleteItem(268)

a = []

# db.table('all').update(
#     {'catalog': 'js'}, doc_ids=a)

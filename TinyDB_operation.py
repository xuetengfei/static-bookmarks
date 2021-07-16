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
    # db.table('all').remove(doc_ids=[162])


goal = {
    'describtion': '培根悖论唠唠嗑',
    'url': 'https://space.bilibili.com/386869863/video',
    "catalog": '因吹斯汀'  # 小写
}

# [培根悖论唠唠嗑的个人空间_哔哩哔哩_Bilibili]()

# AddItem(goal)


# table = db.table('all').update({'catalog': 'x'}, doc_ids=[
# 123, 143, 153, 154, 155, 158, 161])


# db.table('all').update(
#     {'describtion': '如何正确的学习Node.js', 'describe': '如何正确的学习Node.js'}, doc_ids=[4])


# DeleteItem(207)

# https://www.css3maker.com/

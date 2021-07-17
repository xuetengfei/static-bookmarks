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
    'describtion': '圈内师老师',
    'url': 'https://space.bilibili.com/534964283',
    "catalog": '因吹斯汀'  # 小写
}

# AddItem(goal)


# [圈内师老师的个人空间_哔哩哔哩_Bilibili]()

# table = db.table('all').update({'catalog': 'x'}, doc_ids=[
# 123, 143, 153, 154, 155, 158, 161])


# db.table('all').update(
#     {'url': 'https://space.bilibili.com/534964283/video'}, doc_ids=[277])


# DeleteItem(268)

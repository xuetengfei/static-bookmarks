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


goal = {
    'describtion': 'Learn SQL with Socratica',
    'url': 'https://www.youtube.com/playlist?list=PLi01XoE8jYojRqM4qGBF1U90Ee1Ecb5tt',
    "catalog": 'database'  # 小写
}

# AddItem(goal)

# DeleteItem(268)

# table = db.table('all').update({'catalog': 'x'}, doc_ids=[
# 123, 143, 153, 154, 155, 158, 161])


# db.table('all').update(
#     {'describtion': 'Learn SQL with Socratica-youtube'}, doc_ids=[281])

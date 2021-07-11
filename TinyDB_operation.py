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
    'describtion': 'Economic Raven',
    'url': 'https://www.youtube.com/channel/UCj77H54JCFCbKTkIaLC8bRQ',
    "catalog": 'x'  # 小写
}

# AddItem(goal)

# [(4) Economic Raven - YouTube](https://www.youtube.com/channel/UCj77H54JCFCbKTkIaLC8bRQ)
# table = db.table('all').update({'catalog': 'x'}, doc_ids=[
# 123, 143, 153, 154, 155, 158, 161])


# db.table('all').update(
#     {'catalog': 'linux'}, doc_ids=[35])


# DeleteItem(69)


# https://www.css3maker.com/
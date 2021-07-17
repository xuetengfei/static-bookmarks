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
    'describtion': 'Nodejs-Roadmap',
    'url': 'https://github.com/qufei1993/Nodejs-Roadmap',
    "catalog": 'node'  # 小写
}

# AddItem(goal)


# table = db.table('all').update({'catalog': 'x'}, doc_ids=[
# 123, 143, 153, 154, 155, 158, 161])


# db.table('all').update(
#     {'describtion': '如何正确的学习Node.js', 'describe': '如何正确的学习Node.js'}, doc_ids=[4])


# DeleteItem(275)

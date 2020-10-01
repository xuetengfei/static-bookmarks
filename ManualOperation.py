#!/usr/bin/python3
# coding:utf-8

from tinydb import TinyDB, Query, where
from os import sys
import sys
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


# AddItem({
#     'describtion': '端媒体',
#     'url': 'https://theinitium.com/',
#     "catalog": 'x'  # 小写
# })


# table = db.table('all').update({'catalog': 'x'}, doc_ids=[
#     123, 143, 153, 154, 155, 158, 161])


# db.table('all').update(
#     {'describtion': 'My_Github'}, doc_ids=[161])


# # table.remove(doc_ids=[209,210])
# db.table('all').remove(doc_ids=[162])

# print('Remover Item Successed !!!')

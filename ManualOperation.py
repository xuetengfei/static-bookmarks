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
#     'describtion': 'vercel',
#     'url': 'https://vercel.com/dashboard',
#     "catalog": 'x'  # 小写
# })


# table = db.table('all').update({'catalog': 'x'}, doc_ids=[
#     123, 143, 153, 154, 155, 158, 161])


# db.table('all').update(
#     {'describtion': 'My_Github'}, doc_ids=[161])

# DeleteItem(162)


# os.system("sh COMMAND")
os.system(COMMAND)

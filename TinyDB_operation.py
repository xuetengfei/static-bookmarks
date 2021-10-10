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


def DeleteItem(ids):
    db.table('all').remove(doc_ids=ids)
    print('Delete Item Successed !!!')


goal = {
    'describtion': 'HusseinNasser dev channel',
    'detail': '',
    'url': 'https://www.youtube.com/c/HusseinNasser-software-engineering/playlists',
    "catalog": 'dev'  # 小写
    # detail:Add the \n string between any text for multiline tooltips.
}

# AddItem(goal)

# DeleteItem([10, 29, 134, 210, 221, 222, 230])

# db.table('all').update(
#     {'describe': '阮一峰-科技爱好者周刊'}, doc_ids=[74])

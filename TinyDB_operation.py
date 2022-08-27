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

# DeleteItem([362])

# db.table('all').update(
# {'catalog': 'fun'}, doc_ids=[133, 143, 144, 151, 169, 272, 273, 274, 277, 285, 286, 288, 289, 302, 303, 304, 307, 309, 310, 314, 321, 325])

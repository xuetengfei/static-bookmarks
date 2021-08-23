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
    'describtion': 'HusseinNasser dev channel',
    'detail': '',
    'url': 'https://www.youtube.com/c/HusseinNasser-software-engineering/playlists',
    "catalog": 'dev'  # 小写
    # detail:Add the \n string between any text for multiline tooltips.
}

# AddItem(goal)


# a = [223, 224, 227, 231, 267, 278]

# db.table('all').update(
#     {'catalog': 'dev', }, doc_ids=a)


# DeleteItem(298)

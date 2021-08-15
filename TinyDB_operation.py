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


# [浏览器的工作原理：现代网络浏览器幕后揭秘 - HTML5 Rocks]()
goal = {
    'describtion': '浏览器的工作原理',
    'detail': '浏览器的工作原理\n现代网络浏览器幕后揭秘',
    'url': 'https://www.html5rocks.com/zh/tutorials/internals/howbrowserswork/',
    "catalog": 'dev'  # 小写
}

# Add the \n string between any text for multiline tooltips.
# <button class="btn tooltip" data-tooltip="First Line Tooltip Text \n Second Line Tooltip Text">multiline tooltip</button>


# AddItem(goal)

# DeleteItem(293)

a = []

db.table('all').update(
    {'describtion': 'css通用模式', 'detail': 'COLLECTION OF 102 PATTERNS\nCovers are made with CSS only.\n Inspect them!', }, doc_ids=a)

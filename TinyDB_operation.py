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
    'describtion': '10个现代CSS布局',
    'detail': '10个现代CSS布局和大小调整技术\n突出了单行样式代码的健壮性和影响力',
    # Add the \n string between any text for multiline tooltips.
    'url': 'https://1linelayouts.glitch.me/',
    "catalog": 'css'  # 小写
}


# AddItem(goal)

# DeleteItem(293)


a = []
db.table('all').update(
    {'describtion': 'Economic Raven(经济乌鸦)', 'detail': '《经济学乌鸦》是一种简单有趣的每周经济学教材\n没有复杂的图表，没有复杂的公式\n让那些一直想学习的人们更容易理解经济', }, doc_ids=a)

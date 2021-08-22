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


# [(8) the roadmap - YouTube](https://www.youtube.com/c/theroadmap/videos)
goal = {
    'describtion': 'the roadmap channel',
    'detail': '最好的在线web开发和编程讲座和最新的web技术,\n各种计算机科学知识包括系统设计数据库，全栈开发',
    'url': 'https://www.youtube.com/c/theroadmap/videos',
    "catalog": 'dev'  # 小写
    # detail:Add the \n string between any text for multiline tooltips.
}

AddItem(goal)

# DeleteItem(296)


a = []
db.table('all').update(
    {'describtion': 'Economic Raven(经济乌鸦)', 'detail': '经济学乌鸦是一种简单有趣的经济学教材\n没有复杂的图表，没有复杂的公式\n让那些一直想学习的人们更容易理解经济', }, doc_ids=a)

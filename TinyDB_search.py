#!/usr/bin/python3
# coding:utf-8

from tinydb import TinyDB, Query, where
import os
import os.path

p = os.path.abspath(__file__)
path = os.path.abspath(os.path.join(p, os.pardir))+'/db.json'

TinyDB.DEFAULT_TABLE = 'all'
db = TinyDB(path)

ITEM = Query()

print(ITEM)


# db.table('all').remove(doc_ids=[id])

URL = 'https://webcode.tools/generators/css'

goal = db.table('all').search(ITEM.url == URL)
print(goal)


el = db.table('all').get(ITEM.url == URL)
print(el.doc_id)


#  'describtion': 'code-maker-css-html',
#  'url': 'https://webcode.tools/generators/css',
#  "catalog": 'css'  # 小写

# db.table('all').update(
#     {'describtion': 'layouts-patterns-with-CSS'}, doc_ids=[237])

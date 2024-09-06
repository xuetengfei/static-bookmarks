#!/usr/bin/python3
# coding:utf-8

import csv
from tinydb import TinyDB, Query
import os
import os.path

p = os.path.abspath(__file__)
DBFile = os.path.abspath(os.path.join(p, os.pardir)) + "/db.json"  # StaleDBFile

TinyDB.DEFAULT_TABLE = "all"
db = TinyDB(DBFile)
ITEM = Query()


def AddItem(item):
    table = db.table("all")
    table.insert(item)
    print("Insert Successed")


csv_reader = csv.reader(open("./db.csv", encoding="utf-8"))

for line in csv_reader:
    if line:  # 跳过空白行
        if line[0] != "describtion":  # 去掉表头
            o = {}
            o["describtion"] = line[0]
            o["detail"] = line[1]
            o["url"] = line[2]
            o["catalog"] = line[3]
            # print(o)
            el = db.table("all").search(ITEM.url == line[2])
            if len(el) == 0:  # 去重
                AddItem(o)
            # print('Insert Done')

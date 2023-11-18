#!/usr/bin/python3
# coding:utf-8
import csv
from tinydb import TinyDB, Query
import os

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "db.json")
csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "db.csv")

TABLE_NAME = "all"

db = TinyDB(DB_FILE)
ITEM = Query()


def add_item(item):
    table = db.table(TABLE_NAME)
    table.insert(item)
    print("Insert Success")


def process_csv_file(file_path):
    with open(file_path, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header

        for line in csv_reader:
            if line:
                o = {
                    "description": line[0],
                    "detail": line[1],
                    "url": line[2],
                    "catalog": line[3],
                }

                if not db.table(TABLE_NAME).search(ITEM.url == line[2]):
                    add_item(o)


process_csv_file(csv_file_path)


# import csv
# from tinydb import TinyDB, Query
# import os
# import os.path

# p = os.path.abspath(__file__)
# DBFile = os.path.abspath(os.path.join(p, os.pardir)) + "/db.json"  # StaleDBFile

# TinyDB.DEFAULT_TABLE = "all"
# db = TinyDB(DBFile)
# ITEM = Query()


# def AddItem(item):
#     table = db.table("all")
#     table.insert(item)
#     print("Insert Successed")


# csv_reader = csv.reader(open("./db.csv", encoding="utf-8"))

# for line in csv_reader:
#     if line:  # 跳过空白行
#         if line[0] != "describtion":  # 去掉表头
#             o = {}
#             o["describtion"] = line[0]
#             o["detail"] = line[1]
#             o["url"] = line[2]
#             o["catalog"] = line[3]
#             # print(o)
#             el = db.table("all").search(ITEM.url == line[2])
#             if len(el) == 0:  # 去重
#                 AddItem(o)
#             # print('Insert Done')

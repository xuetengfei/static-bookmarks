#!/usr/bin/python3
# coding:utf-8

import csv
from tinydb import TinyDB, Query
import os

# 获取数据库文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(current_dir, "db.json")

# 初始化数据库
TinyDB.DEFAULT_TABLE = "all"
db = TinyDB(DB_FILE)
Item = Query()

def add_item(item):
    """添加一个条目到数据库"""
    db.insert(item)
    print("Insert Succeeded")

# 读取CSV文件
with open("db.csv", "r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        # 创建条目字典
        item = {
            "description": row["describtion"],  # 注意：这里保留了原有的拼写错误
            "detail": row["detail"],
            "url": row["url"],
            "catalog": row["catalog"]
        }
        
        # 检查是否存在相同URL的条目
        if not db.contains(Item.url == item["url"]):
            add_item(item)

print("All items processed")

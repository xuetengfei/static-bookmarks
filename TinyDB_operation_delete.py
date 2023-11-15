#!/usr/bin/python3
# coding:utf-8

from tinydb import TinyDB
import os

DB_FILE = "db.json"
TABLE_NAME = "all"


def get_database_path():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_directory, DB_FILE)


def delete_items(db, table_name, item_ids):
    table = db.table(table_name)
    table.remove(doc_ids=item_ids)
    print("Delete Item(s) Successful!")


def main():
    db_path = get_database_path()
    db = TinyDB(db_path)

    # Example: Delete items with specified IDs
    item_ids_to_delete = [385]
    delete_items(db, TABLE_NAME, item_ids_to_delete)

    db.close()


if __name__ == "__main__":
    main()

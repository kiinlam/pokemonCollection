#使用pymongo操作数据库

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemon"]
col_index = db["index"]


def find_all():
    return col_index.find({}, skip=0)


def insert_list(datalist):
    if datalist:
        print('插入数据库{}条数据'.format(len(datalist)))
        return col_index.insert_many(datalist)


def update_detail(query, data):
    if data:
        print('插入数据库1条数据:', data)
        return col_index.update_one(query, {"$set": data})


def main():
    print(__name__)


if __name__ == '__main__':
    main()
else:
    print(__name__)

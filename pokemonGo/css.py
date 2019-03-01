#使用tinycss2解析css样式文件，提取精灵属性名与对应颜色值，写入数据库

import re
import tinycss2 as tc
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pokemon"]
col_color = db["color"]
count = 0


def insert_one(insert_data):
    return col_color.insert_one(insert_data)


with open("color.css", "r") as f:
    line = f.read()
    rules = tc.parse_stylesheet(line, skip_comments=True, skip_whitespace=True)
    for rule in rules:
        key = "".join([x.value for x in rule.prelude])
        if ("pokemon-type__type--" in key) and (":" not in key):
            # 类型英文名
            value = "".join([str(x.value) for x in rule.content])
            # 类型颜色值
            color = re.search("background-color: (.*);", value).group(1)
            if len(color) is 3:
                color *= 2
            data = {
                "_id": key.split("pokemon-type__type--")[1],
                "color": color
            }
            count += 1
            insert_one(data)

print(count)


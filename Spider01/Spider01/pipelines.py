# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter


class Spider01Pipeline:
    def __init__(self):
        self.file = open('douban.json', 'w', encoding="utf-8")

    def process_item(self, item, spider):
        # 将python转化为json格式数据保存
        json_data = json.dumps(item, ensure_ascii=False) + ',\n'
        self.file.write(json_data)
        return item

    def __del__(self):
        self.file.close()

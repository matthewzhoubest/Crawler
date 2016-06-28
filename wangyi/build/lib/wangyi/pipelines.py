# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class WangyiPipeline(object):
    def __init__(self):
        self.file = open('items.json', 'w')
    def process_item(self, item, spider):
        #if item['url'].startswith('http://news.163.com') or item:
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
        #else:
        #    raise DropItem('Not news item %s' % item)

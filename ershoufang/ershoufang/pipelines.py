# -*- coding: utf-8 -*-
import json
import codecs

#以Json的形式存储
class ErshoufangPipeline(object):
    def __init__(self):
        self.file = codecs.open('ershoufang.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        line = line + ','
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

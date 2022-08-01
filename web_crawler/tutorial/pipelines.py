# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import re


class TutorialPipeline:
    double_quotes = '|'.join([chr(ord('\u201c')), chr(ord('\u201d'))])
    single_quotes = '|'.join([chr(ord('\u2019')), chr(ord('\u2032'))])
    dashes = '|'.join([chr(ord('\u2014'))])

    def open_spider(self, spider):
        self.results = []

    def process_item(self, item, spider):
        _item = ItemAdapter(item).asdict()

        # Remove the fancy characters
        _item['text'] = re.sub(fr'{self.double_quotes}', '', _item['text'])
        _item['text'] = re.sub(fr'{self.single_quotes}', "'", _item['text'])
        _item['text'] = re.sub(fr'{self.dashes}', '---', _item['text'])

        self.results.append(_item)
        return _item

    def close_spider(self, spider):
        with open('results.json', 'w') as export_file:
            json.dump(self.results, export_file, indent=2)

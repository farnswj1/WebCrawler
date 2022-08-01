# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class TutorialPipeline:
    def open_spider(self, spider):
        self.results = []

    def process_item(self, item, spider):
        self.results.append(ItemAdapter(item).asdict())
        return item

    def close_spider(self, spider):
        with open('results.json', 'w') as export_file:
            json.dump(self.results, export_file, indent=2)

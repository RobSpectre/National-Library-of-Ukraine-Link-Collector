# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exporters import CsvItemExporter

from nlu_link_collector.items import NluLinkCollectorItem


class NluLinkCollectorPipeline:
    def open_spider(self, spider):
        self.file = open('{0}_links.csv'.format(spider.name),
                         'w+b')

        self.exporter = CsvItemExporter(self.file)

    def close_spider(self, spider):
        self.exporter.finish_exporting()

        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, NluLinkCollectorItem):
            self.exporter.export_item(item)
        return item

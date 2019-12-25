# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter, JsonItemExporter

class AutoPricePipeline(object):
    def __init__(self):
        self.file = open('data/autoPrice.csv','wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()
    def open_spider(self,spider):
        pass
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


class amapPipeline(object):
    def __init__(self):
        self.file = open('../../data/amapTel.csv','wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()
    def open_spider(self,spider):
        pass
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


class CarPricePipeline(object):
    def open_spider(self,spider):
        self.file = open('../../data/CarPrice.csv','wb')
        self.exporter = CsvItemExporter(self.file)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
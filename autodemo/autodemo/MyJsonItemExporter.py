
from scrapy.exporters import JsonItemExporter

from autodemo import settings


class MyJsonItemExporter(JsonItemExporter):

    def __init__(self, *args, **kwargs):
        FEED_EXPORT_FIELDS = settings.FEED_EXPORT_FIELDS
        kwargs['FEED_EXPORT_FIELDS'] = FEED_EXPORT_FIELDS
        kwargs['FEED_EXPORT_ENCODING'] = settings.FEED_EXPORT_ENCODING

        super(MyJsonItemExporter, self).__init__(*args, **kwargs)
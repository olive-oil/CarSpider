import json
import logging
from math import ceil

from autodemo.items import PoiItem
import scrapy
#爬取高德地图租车信息（商户、地址、电话）
class AmapSpider(scrapy.Spider):
    name = 'amapPhone'
    allow_domains = 'www.amap.com'
    start_urls = ['https://restapi.amap.com/v3/place/text?key=d0de733aaee4bda8f95c2b672d757024&city=500000&citylimit=true&types=010900|010901&children=1&page=0']
    custom_settings = {
        'ITEM_PIPELINES': {
            'autodemo.pipelines.amapPipeline': 200
        },
    }
    def parse(self, response):
        logging.info(response.url)
        detail = json.loads(response.text)
        page_len = ceil(int(detail['count']) / 20)
        for i in range(page_len):
            next_url = 'https://restapi.amap.com/v3/place/text?key=d0de733aaee4bda8f95c2b672d757024&city=500000&citylimit=true&types=010900|010901&children=1&page=%d' % i
            logging.info('url is %s' % next_url)
            yield scrapy.Request(url= next_url, callback= self.parse_detail)

    def parse_detail(self,response):
        detail = json.loads(response.text)
        status = int(detail['status'])
        if (response.status == 200 and status == 1):
            pois = detail['pois']
            for poi in pois:
                poiItem = PoiItem()
                poiItem['name'] = poi['name']
                poiItem['address'] = poi['address']
                poiItem['longitude'] = poi['location'].split(",")[0]
                poiItem['latitude'] = poi['location'].split(",")[1]
                if(";" in poi['tel']):
                    poiItem['tel1'] = "".join(poi['tel']).split(";")[0]
                    poiItem['tel2'] = "".join(poi['tel']).split(";")[1]
                elif(poi['tel']):
                    poiItem['tel1'] = poi['tel']
                yield poiItem
import scrapy
from autodemo.items import CarItem
#爬取汽车之家车系信息（大类）
class AutoSpiders(scrapy.Spider):
    name = 'carPrice'
    allowed_domains = 'autohome.com.cn'
    start_urls = ['https://www.autohome.com.cn/grade/carhtml/%s.html' % chr(ord('A') + i) for i in range(26)]
    custom_settings = {
        'ITEM_PIPELINES':{
            'autodemo.pipelines.CarPricePipeline': 200
        }
    }

    def parse(self, response):
        for brandPath in response.xpath('body/dl'):
            brand = CarItem()
            brand['car'] = brandPath.xpath('dt/div/a/text()').extract()
            for carPath in brandPath.xpath('dd/ul/li'):
                if(not carPath.re(r'指导价：暂无')):
                    brand['price'] = carPath.xpath('div/a[starts-with(@class,"red")]/text()').extract()
                else:
                    brand['price'] = ''
                yield brand


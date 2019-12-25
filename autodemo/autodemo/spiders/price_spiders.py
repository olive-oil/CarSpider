import re

import scrapy
import logging
from scrapy.spiders import Rule, CrawlSpider, XMLFeedSpider

from autodemo.items import SpecificItem
from scrapy.linkextractors import LinkExtractor
#爬取汽车之家车系信息（小类）
class price_spiders(CrawlSpider, XMLFeedSpider):
    name = "priceDemo"
    allowed_domains = 'autohome.com.cn'
    start_urls = ['https://www.autohome.com.cn/grade/carhtml/%s.html' % chr(ord('A') + i) for i in range(26)]
    custom_settings = {
        'ITEM_PIPELINES': {
            'autodemo.pipelines.AutoPricePipeline': 200
        }
    }

    rules = (
        # 字母分区
        Rule(LinkExtractor(allow=(r'https://www.autohome.com.cn/grade/carhtml/[A-Z].html')), callback='parse',follow=True),
        # 车系详情页
        Rule(LinkExtractor(allow=(r'https://www.autohome.com.cn/\d+/#levelsource=000000000_0&pvareaid=101594')), callback='parse_auto_selling', follow=True),
    )
    #字母分区页解析
    def parse(self, response):
        logging.info('[parse] %s' % response.url)
     #解析车系
        for series_page_url in  response.xpath('body/dl/dd/ul/li/h4/a/@href').extract():
            url = "https://"+series_page_url
            logging.info('[series_page_url] is : %s' % url)
            request = scrapy.Request(url=url, callback=self.parse_auto_selling, dont_filter=True)
            yield request

    #详细车系信息解析
    def parse_auto_selling(self, response):
        spcItem = SpecificItem()
        for carPath in response.xpath('body'):
            #停售
            if(carPath.re(r'指导价（停售）')):
                # 停售车两种页面
                car = response.xpath('//body/div/div/div/div[@class="subnav-title-name"]/a/text()').extract()
                if(car is not None):
                    spcItem['car'] = '停售款：'+"".join(car)
                    spcItem['source_img'] = response.xpath('//*[starts-with(@class,"models_pics")]/dt/a/img/@src').extract()
                    group = response.xpath('//*[starts-with(@class,"name_d")]/div/a/@title').extract()
                    price = response.xpath('//*[starts-with(@class,"price_d")]/div/text()').extract()
                    reference_price = response.xpath('//*[starts-with(@class,"price_d")]/span[@class="red price02"]').extract()
                    for i in range(len(group)):
                        spcItem['group'] = group[i]
                        spcItem['price'] = price[i]
                        pattern = re.compile(r'>([^<>]+?)<')
                        spcItem['reference_price'] = re.findall(pattern, reference_price[i])
                        yield spcItem
                #另一种停售车页面
                else:
                    car = '停售款：'+\
                          response.xpath('//body/div[1]/div[3]/div[2]/div[1]/div[1]/a/text()').extract()[0]+\
                          response.xpath('//body/div[1]/div[3]/div[2]/div[1]/div[1]/a/h1/text()').extract()[0]
                    spcItem['car'] = car
                    spcItem['source_img'] = response.xpath('//*[starts-with(@class,"pic-main")]/a/picture/source/@srcset').extract()
                    group = response.xpath('//*[starts-with(@id,"spec_")]/a/text()').extract()
                    price = response.xpath('//*[@id="specWrap-2"]/dl/dd/div[3]/p/span/text()').extract()
                    spcItem['reference_price'] = response.xpath('//*[@id="series_che168"]/em/text()').extract()
                    for i in range(len(group)):
                        spcItem['group'] = group[i]
                        spcItem['price'] = price[i]
                        yield spcItem
            #在售车
            else:
                spcItem['car'] = '在售款：'+"".join(response.xpath('//*[@class="athm-title__name athm-title__name--blue"]/a/text()').extract()[0])
                group = response.xpath('//*[starts-with(@id,"spec_")]/a/text()').extract()
                price = response.xpath('//*[@id="specWrap-2"]/dl/dd/div[3]/p/span/text()').extract()
                spcItem['reference_price'] = response.xpath('//*[starts-with(@id,"series_che")]/em/text()').extract()
                spcItem['source_img'] = response.xpath('//*[starts-with(@id,"picture-1")]/li/a/@href').extract()
                for i in range(len(group)):
                    spcItem['group'] = group[i]
                    spcItem['price'] = price[i]
                    yield spcItem

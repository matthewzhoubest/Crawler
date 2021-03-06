# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from wynews.items import WynewsItem
from scrapy.http import Request

class WynewsSpider(BaseSpider):
    name = "Wynews"

    def __init__(self, category=None, *args, **kwargs):
        super(WynewsSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://news.163.com/rank/']
        if category=='all':
            self.category=''
        else:
            self.category = category


    def parse(self,response):
        html = HtmlXPathSelector(response)
        page = html.xpath('//div[@class="subNav"]/a')
        for i in page:
            item = dict()
            if self.category in i.xpath('text()').extract_first():
                item['category'] = i.xpath('text()').extract_first()
                item['url'] = i.xpath('@href').extract_first()
                print item['category'],item['url']
                yield Request(url=item['url'],meta={'item_1': item},callback=self.second_parse)

    def second_parse(self,response):
        item_1= response.meta['item_1']
        html = HtmlXPathSelector(response)
        #print 'response ',response
        page = html.xpath('//tr/td/a')
        #print 'page ',page
        items = []
        for i in page:
            item = WynewsItem()
            item['category'] = item_1['category'].encode('utf8')
            item['url'] = item_1['url'].encode('utf8')
            item['secondary_title'] = i.xpath('text()').extract_first().encode('utf8')
            item['secondary_url'] = i.xpath('@href').extract_first().encode('utf8')
            #print i.xpath('text()').extract(),i.xpath('@href').extract()
            items.append(item)
        return items

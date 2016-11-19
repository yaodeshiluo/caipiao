# coding: utf-8
import scrapy
from v1.items import V1Item
import json
from v1.helper import getlist, url_handler
from scrapy import Request

class Spider1(scrapy.spiders.Spider):
    name = 'v1'


    def __init__(self, category="shuangseqiu", *args, **kwargs):
        super(Spider1, self).__init__(*args, **kwargs)
        self.crawl_list = getlist(category)
        self.start_urls = [self.crawl_list[0].get('website')]
        self.id = 0
        self.url_count = 0

    def parse(self,response):
        print 'crawl_list is',len(self.crawl_list)
        print 'id is', self.id
        sel = response.selector
        url_sel = sel.xpath(self.crawl_list[self.id].get('urllist'))
        print url_sel
        url_sel = url_handler(url_sel,response.url)
        print 'url_sel is', len(url_sel)
        self.url_count = len(url_sel)
        for i in url_sel:
            yield Request(i, callback=self.parse_info)

    def parse_info(self,response):
        sel = response.selector
        item = V1Item()
        item['balance'] = sel.xpath(self.crawl_list[self.id].get('balance') + '/text()').extract()[0]
        item['name'] = self.crawl_list[self.id].get('name')
        item['issue'] = sel.xpath(self.crawl_list[self.id].get('issue')+'/text()').extract()[0]
        item['key'] = self.crawl_list[self.id].get('key')
        item['open_time'] = sel.xpath(self.crawl_list[self.id].get('open_time')+'/text()').extract()[0]
        item['result'] = sel.xpath(self.crawl_list[self.id].get('result')+'/text()').extract()
        item['sales'] = sel.xpath(self.crawl_list[self.id].get('sales')+'/text()').extract()[0]
        item['src'] = self.crawl_list[self.id].get('src')

        detail_table = sel.xpath(self.crawl_list[self.id].get('detail'))
        detaillist = []
        tr1 = detail_table.xpath('//tr[1]/th/text()').extract()
        for i in range(1,len(detail_table.xpath('//tr'))):
            each_tr = detail_table.xpath('//tr[%s]/td/text()'%(i+1)).extract()
            adict = {}
            for j in range(len(tr1)):
                adict = {}
                adict[tr1[j]] = each_tr[j]
            detaillist.append(adict)
        item['detail'] = detaillist
        self.url_count -= 1
        yield item

        print 'url_count is', self.url_count

        if self.url_count ==0:
            self.id += 1
            try:
                adict_of_crawl_list = self.crawl_list[self.id]
            except:
                print 'no more request'
            else:
                yield Request(self.crawl_list[self.id].get('website'),callback=self.parse)





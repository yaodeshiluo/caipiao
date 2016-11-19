# coding: utf-8
import scrapy
from tutorial.items import TutorialItem

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

class Dmozspider(scrapy.spiders.Spider):
    name = 'dmoz'
    allowed_domains = 'cwl.gov.cn'
    start_urls = [
        'http://www.cwl.gov.cn/kjxx/ssq/kjgg/406698.shtml',
        'http://www.cwl.gov.cn/kjxx/ssq/kjgg/406644.shtml'
    ]

    # def parse(self,response):
    #     filename = response.url.split('/')[-2]
    #     with open(filename,'wb') as f:
    #         f.write(response.body)

    def parse(self,response):
        item = TutorialItem()
        sel = response.selector
        table = sel.xpath('//div[@class="drawright"]')

        # for each in table.xpath('ul/li[1]/span'):
        #     print each.xpath('string(.)').extract()[0]
        item['issue'] = table.xpath('ul/li[1]/span[1]/text()').extract()[0]
        item['date'] = table.xpath('ul/li[1]/span[2]/text()').extract()[0].split(u'：')[-1]
        item['sales_of_this_issue'] = table.xpath('ul/li[1]/span[3]').xpath('string(.)').extract()[0].split(u'：')[-1]
        item['jackpot'] = table.xpath('ul/li[1]/span[4]').xpath('string(.)').extract()[0].split(u'：')[-1]
        # print table.xpath('ul/li[2]/i/text()').extract()[0]
        # for each in table.xpath('ul/li[2]/span/text()').extract():
        #     print each
        item['numbers'] = ','.join(table.xpath('ul/li[2]/span/text()').extract())
        prize_info = {}
        i = 0
        for each in table.xpath('table/tbody/tr'):
            td_list = each.xpath('td/text()').extract()
            # for i in range(len(td_list)):
            #     print td_list.extract()[i]
            eachline = ' '.join(td_list)
            prize_info[i] = eachline
            i += 1
        item['prize_info'] = prize_info

        yield item









import json
import re

def getlist(category):
    alist=[]
    with open(r'D:\virtualenv\caipiao\v1\v1\spiders\query.json', 'r') as f:
        query = json.load(f)
        if '&&' in category:
            caizhong = category.split('&&',1)[0]
            website = category.split('&&',1)[1]
            for i in query:
                print i.get('caizhong') == caizhong
                print i.get('website') == website
                if i.get('caizhong') == caizhong and i.get('website') == website:
                    print i.get('caizhong') == caizhong
                    alist.append(i)
        else:
            for i in query:
                if i.get('caizhong') == category:
                    alist.append(i)

    return alist

def url_handler(urllist,response_url):
    if response_url is 'http://www.cwl.gov.cn/kjxx/ssq/hmhz/':
        alist = []
        baseurl = 'http://www.cwl.gov.cn/kjxx/ssq/kjgg/'
        for i in urllist.extract():
            url = baseurl + i.split('/')[-1]
            alist.append(url)
        return alist
    elif response_url is 'http://caipiao.163.com/award/ssq/':
        alist = []
        latest_num = urllist.xpath('text()').extract()[0]
        for i in range(20):
            url = response_url + '%s'%(latest_num - i) + '.html'
            alist.append(url)
        return alist


    return urllist






import json
with open(r'D:\virtualenv\caipiao\v1\items3.json','r') as f:
    out = json.load(f)
    for i in out:
        for k,v in i['detail'].iteritems():
            print k,v



#coding=utf-8

import requests
import json
import time
import csv
import codecs

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.113 Safari/537.36'
}
url = 'https://sec.wedengta.com/getIntelliStock?action=IntelliSecPool&id=99970_56&_={0}'.format(time.time())
r = requests.get(url, headers=headers)
result = json.loads(r.text)

rows = []
for every in json.loads(result['content'])['vtDaySec']:
    for company in every['vtSec']:
        row = (
            every['sOptime'].encode('utf-8'),
            company['sChnName'].encode('utf-8'),
            company['sDtCode'][4:].encode('utf-8')
        )
        rows.append(row)

with codecs.open('company.csv', 'wb') as f:
    f.write(codecs.BOM_UTF8)
    writer = csv.writer(f)
    writer.writerow(['date', 'stk_name', 'stk_num'])
    writer.writerows(rows)

# 网页抓包， curl格式导出。 贴到postman做好测试， 然后使用code-python-requests格式导出代码。

#see page:  https://careers.tencent.com/search.html?index=1    目前有258页.page10的情况下

# 导入requests库
import requests
# 导入文件操作库
import os
import bs4
from bs4 import BeautifulSoup
import sys
import importlib
import random
import time
import pandas as pd
# 越多越好
meizi_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
]
# 给请求指定一个请求头来模拟chrome浏览器
global headers
headers = {'User-Agent': random.choice(meizi_headers),
           'accept-encoding': 'gzip, deflate, br',
           'accept': 'application/json, text/plain, */*',
           'referer': 'https://careers.tencent.com/search.html',
           'authority': 'careers.tencent.com',
           'cookie': '_ga=GA1.2.539901423.1561958440; pgv_pvi=8552522752; _gcl_au=1.1.1776428619.1561958441;'
                     ' __root_domain_v=.tencent.com; _qddaz=QD.62k0ox.lb2mjl.jxjxq9xh; pgv_pvid=284433220;'
                     ' ___rl__test__cookies=1564040214742; OUTFOX_SEARCH_USER_ID_NCOO=1268259490.5845864; loading=agree'}
page = 1  # 从1开始
pageSize = 30

result_list = []
for i in range(1,1000):
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?' \
          'timestamp=%d&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=%d&pageSize=%d&language=zh-cn&area=cn' % (
          time.time(), page, pageSize)
    print('fetch-page-%d' % page)
    res_sub = requests.get(url, headers=headers)
    rsp= res_sub.json()
    if rsp['Code'] != 200:
        print("Err-got. %s" % rsp)
        continue
    else:
        if rsp['Data']['Posts'] is None or len(rsp['Data']['Posts']) == 0:
            print("ends....")
            break
        result_list.extend(rsp['Data']['Posts'])
    page+=1

print('total %d' % len(result_list))
pd.DataFrame(result_list).to_csv("hello.csv")
# 使用爬虫有道翻译

import urllib.request
import urllib.parse
import json
import time

while True:
    content = input("请输入需要翻译的内容：\n")

    url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    # 需要去掉链接中的_o

    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '16186591002498'
    data['sign'] = '30c4f3c8186d783edd586a1317a97d59'
    data['lts'] = '1618659100249'
    data['bv'] = '12a0fdafaf07590af9277366a5ee886b'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] =' FY_BY_REALTlME'
    data = urllib.parse.urlencode(data).encode('utf-8')
    # 据说只需传入 i 和 doctype 即可，其余的不需要

    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')


    target = json.loads(html)
    print("翻译结果：\n %s " % (target['translateResult'][0][0]['tgt']))
    time.sleep(3) # 休眠3秒后再进行下一次操作

                                  
                                


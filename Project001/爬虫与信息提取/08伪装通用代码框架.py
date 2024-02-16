#伪装通用代码框架.py
import requests
kv={'user-agent':'Mozilla/5.0'}#爬虫模拟浏览器，浏览器身份识别字段
url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    r=requests.get(url,headers=kv)#,timeout=30)
    r.raise_for_status()#判断访问是否成功
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except requests.HTTPError:
    print("产生异常")
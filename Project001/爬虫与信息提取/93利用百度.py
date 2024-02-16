#利用百度搜索.py
import requests
keyword="Python"
try:
    kv={'wd':'keyword'}#wd是百度关键词的接口，把wd改成q就能用于360搜索引擎
    r=requests.get("http://www.baidu.com/s",params=kv)
    print(r.request.url)#查看我方发给对方的Request包含的Url是什么
    #返回：'http://www.baidu.com/s?wd=Python'
    r.raise_for_status()#返回值若不是200则报错
    print(len(r.text))#返回：1302829
except requests.HTTPError:
    print("爬取失败")
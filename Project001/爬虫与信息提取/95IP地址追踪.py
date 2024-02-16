#IP地址追踪.py
#IPO接口：http://m.ip138.com/ip.asp?ip=ipaddress
import requests
ip="218.19.45.212&action=2"
url="https://www.ip138.com/iplookup.php?ip="
kv={'user-agent':'Mozilla/5.0'}#爬虫模拟浏览器，浏览器身份识别字段
try:
    r=requests.get(url+ip,headers=kv)#,timeout=30)
    r.raise_for_status()#判断访问是否成功
    r.encoding=r.apparent_encoding
    print(r.text[-500:])
except requests.HTTPError:
    print("产生异常")
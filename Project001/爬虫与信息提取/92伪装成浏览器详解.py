#伪装成浏览器.py
import requests
r=requests.get("https://www.amazon.cn/gp/product/B01M8L5Z3Y")
r.status_code#返回503
r.encoding#返回'ISO-8859-1'
r.encoding=r.apparent_encoding
r.text#返回……AIP……意外错误……，表示不是网络问题，而是网站问题，被限制了
#网站限制手段：一、Robots协议，二、对网站访问的HTTP头部进行判断是否爬虫
r.request.headers#查看从我方发给对方的head内容
#返回：{'Accept':'*/*','Accept-Encoding':'gzip,deflate','User-Agent':
#'python-requests/2.11.1','Connection':'keep-alive'}
kv={'user-agent':'Mozilla/5.0'}#爬虫模拟浏览器，浏览器身份识别字段
url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
r=requests.get(url,headers=kv)
r.status_code
#返回200，访问成功
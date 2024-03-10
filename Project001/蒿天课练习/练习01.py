# bs4伪装通用框架.py
import requests
from bs4 import BeautifulSoup

kv = {"user-agent": "Mozilla/5.0"}  # 爬虫模拟浏览器，浏览器身份识别字段
url = "http://python123.io/ws/demo.html"
try:
    r = requests.get(url, headers=kv)  # ,timeout=30)
    r.raise_for_status()  # 判断访问是否成功
    r.encoding = r.apparent_encoding
    # print(r.text)
except requests.HTTPError:
    print("产生异常")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")  # 解析demo需要解释器“html.parser”
soup.title
soup.a.name
print(soup.a.name)
print(soup.a.parent.name)
print(soup.a.parent.parent.name)
tag=soup.a
tag.attrs
tag.attrs['class']
tag.attrs['href']
type(tag.attrs)
type(tag)
soup.a
soup.a.string
soup.title
soup.title.string
soup.p
soup.p.string
type(soup.p.string)
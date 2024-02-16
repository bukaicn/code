#爬取网页通用代码框架.py
import requests
url="https://item.jd.com/2967929.html"
def p():
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except requests.HTTPError:
        return "产生异常"
print(p()[:1000])
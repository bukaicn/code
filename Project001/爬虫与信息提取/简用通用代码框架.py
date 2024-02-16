#简用通用代码框架.py
import requests
url="https://item.jd.com/2967929.html"
try:
    r=requests.get(url)#,timeout=30)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except requests.HTTPError:
    print("产生异常")
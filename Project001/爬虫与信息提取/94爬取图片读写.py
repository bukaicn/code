import requests
import os
url="https://www.natgeoexpeditions.com.au/content/images/Kimberley.jpg"
root="d:/1/"
path=root+url.split('/')[-1]
kv={"user-agent":"Mozilla/5.0"}#爬虫模拟浏览器，浏览器身份识别字段
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url,headers=kv,timeout=30)
        print(r.status_code)#200
        r.raise_for_status()
        with open(path,'bw') as f:
            f.write(r.content)#r.content表示Response返回图片的二进制形式，写入变量f中
            print("文件保存成功")
    else:
        print("文件已经存在")
except requests.HTTPError:
    print("产生异常")
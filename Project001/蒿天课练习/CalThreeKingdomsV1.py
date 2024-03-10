#CalThreeKingdomsV1.py
import jieba
txt=open("threekingdoms.txt","r",encoding="utf-8").read()
for i in "曰,二人,却说,不可,荆州,不能,如此,商议,如何":
    txt=txt.replace(i,"")
txt=txt.replace("丞相","曹操")
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1#每一次循环取词，该词的键值+1，get取原有数量
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
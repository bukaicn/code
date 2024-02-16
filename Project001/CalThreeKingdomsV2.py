#CalThreeKingdomsV2.py
import jieba
txt=open("threekingdoms.txt","r",encoding="utf-8").read()
excludes={"二人","却说","不可","荆州","不能","商议"\
          ,"如此","将军","如何","军士","左右","军马","引兵","次日","大喜"\
          ,"天下","东吴","于是","今日"}
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="诸葛亮"or word=="孔明曰":
        rword="孔明"
    elif word=="关公"or word=="云长":
        rword="关羽"
    elif word=="玄德"or word=="玄德曰"or word=="主公":
        rword="刘备"
    elif word=="孟德"or word=="丞相":
        rword="曹操"
    else:
        rword=word
    counts[rword]=counts.get(rword,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
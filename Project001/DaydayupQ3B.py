#DaydayupQ3B.py
dayfactor=0.01
x=1
for i in range(365):
    if i%7 in [6,0]:
        x*=(1-dayfactor)
    else:
        x*=(1+dayfactor)
print("工作日的力量:{:.0f}%".format(x*100))
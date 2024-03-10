#DaydayupQ3.py
dayfactor=0.01
x=1
for i in range(52):
    x*=pow(1+dayfactor,5)
    x*=pow(1-dayfactor,2)
print("工作日的力量:{:.0f}%".format(x*100))
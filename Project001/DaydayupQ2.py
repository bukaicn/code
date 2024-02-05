#DaydayupQ2.py
dayfactor=0.01
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365)
print("向上:{:.0f}%,向下:{:.0f}%".format(dayup*100,daydown*100))
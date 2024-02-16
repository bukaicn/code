#基本统计值计算.py
def median(numbers):#求中位数
    sorted(numbers)
    size=len(numbers)
    if size%2==0:
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med=numbers[size//2]
    return med
def get():#获取用户输入
    x=input("请输入一组数据：")
    y=[]
    while x!="":
        y.append(eval(x))
        x=input("请输入一组数据：")
    return y
def pin(numbers):#求平均值
    a=0.0
    for b in (numbers):
        a+=b
    return(a/len(numbers))
def dev(numbers,mean):#计算方差
    sdev=0.0
    for num in numbers:
        sdev=sdev+(sdev-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)
y=get()
print("平均值：{}方差：{:.2f}中位数{}".format(pin(y),dev(y,pin(y)),median(y)))
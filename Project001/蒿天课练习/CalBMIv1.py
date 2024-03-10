#CalBMIv1.py
h,w=eval(input("请输入身高(m)和体重(kg)[英文逗号隔开]"))
b=w/pow(h,2)
print("BMI数值为：{:.2f}".format(b))
if b<18.5:
    w="偏瘦"
elif b<25:
    w="正常"
elif b<30:
    w="偏胖"
else:
    w="肥胖"
print("BMI指标为：国际'{}'".format(w))
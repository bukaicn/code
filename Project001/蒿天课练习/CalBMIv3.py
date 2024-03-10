#CalBMIv1.py
h,w=eval(input("请输入身高(m)和体重(kg)[英文逗号隔开]："))
b=w/pow(h,2)
print("BMI数值为：{:.2f}".format(b))
if b<18.5:
    gb,iso="偏瘦","偏瘦"
elif b<24:
    gb,iso="正常","正常"
elif b<25:
    gb,iso="偏胖","正常"
elif b<28:
    gb,iso="偏胖","偏胖"
elif b<30:
    gb,iso="肥胖","偏胖"
else:
    gb,iso="肥胖","肥胖"
print("BMI指标为：{}(国内)，{}(国外)".format(gb,iso))
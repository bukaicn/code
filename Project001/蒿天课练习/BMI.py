print("身体质量指数BMI是国际惯用的衡量人体肥胖和健康程度的重要标准")
m,kg=-1,-1
while m<0 or kg<0:
    try:
        m=eval(input("请输入身高(m)："))
        kg=eval(input("请输入体重(kg)："))
    except:  # noqa: E722
        print("请按提示输入")
b=kg/pow(m,2)
print("BMI数值为：{:.1f}".format(b))
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
print("BMI指标为：{}(中国人)，{}(外国人)".format(gb,iso))
print("BMI=体重(kg)/身高(m)的平方")
print("国内定义18.5~24之间为正常，低于该值为偏瘦，高则偏胖，超过28为肥胖")
print("国外定义18.5~25之间为正常，低于该值为偏瘦，高则偏胖，超过30为肥胖")
print("祝您好运！")
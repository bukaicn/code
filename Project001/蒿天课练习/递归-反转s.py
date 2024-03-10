#递归-反转s.py
def rvs(s):
    if s=="":
        return s
    else:
        return rvs(s[1:])+s[0]
s=input("请输入：")
print(rvs(s))
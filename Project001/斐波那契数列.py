#斐波那契数列.py
def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
n=input("请输入：")
print(f(eval(n)))
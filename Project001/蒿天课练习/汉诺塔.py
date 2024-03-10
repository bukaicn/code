#汉诺塔.py
count=0
def hanoi(n,src,dst,mid):
    global count
    if n==1:
        print("{}:{}->{},".format(1,src,dst),end="")
        count+=1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{},".format(n,src,dst),end="")
        count+=1
        hanoi(n-1,mid,dst,src)
n=input("请输入：")
hanoi(eval(n),"A","C","B")
print("\n共{}步".format(count))
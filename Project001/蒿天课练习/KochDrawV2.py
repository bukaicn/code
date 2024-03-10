#KochDrawV1.py
import turtle as t
def koch(size,n):
    if n==0:
        t.fd(size)
    else:
        for angle in (0,90,-90,-90,90):
            t.left(angle)
            koch(size/3,n-1)
def main():
    x=input("请输入(建议1~4)：")
    y=400
    t.setup(800,800)
    t.penup()
    t.goto(-300,200)
    t.pendown()
    t.pensize(2)
    koch(y,eval(x))
    t.right(90)
    koch(y,eval(x))
    t.right(90)
    koch(y,eval(x))
    t.right(90)
    koch(y,eval(x))
    t.hideturtle()
    t.done()
main()
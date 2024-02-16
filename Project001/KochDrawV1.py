#KochDrawV1.py
import turtle as t
def koch(size,n):
    if n==0:
        t.fd(size)
    else:
        for angle in (0,60,-120,60):
            t.left(angle)
            koch(size/3,n-1)
def main():
    x=input("请输入(建议1~4)：")
    t.setup(800,800)
    t.penup()
    t.goto(-300,200)
    t.pendown()
    t.pensize(2)
    koch(600,eval(x))
    t.right(120)
    koch(600,eval(x))
    t.right(120)
    koch(600,eval(x))
    t.hideturtle()
    t.done()
main()
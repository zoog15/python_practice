import turtle

t = turtle.Turtle()
t.shape("turtle")

def func(x) :
    return x**2+1

t.goto(200,0) # x축 그리기
t.goto(0,0)

t.goto(0,200) # y축 그리기
t.goto(0,0)

for x in range(0,151) :
    t.goto(x,int(0.01*func(x)))


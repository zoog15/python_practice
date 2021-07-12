import turtle
import random

t = turtle.Turtle()
s = turtle.Screen() #객채선

def draw_shape(t,c,length,sides,x,y) : #랜덤으로 도형을 그리는 함수 선언
    t.up()
    t.goto(x,y)
    t.down()
    t.fillcolor(c) #c에 해당하는 색깔로 도형 채움
    angle = 360.0 / sides 
    t.begin_fill()
    for dist in range(sides) :
        t.forward(length)
        t.left(angle)
    t.end_fill()

for i in range(10) :
    color = random.choice(['white','yellow','blue','skyblue','orange','green'])
    side_length = random.randint(10,100)
    sides = random.randint(3,10)
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    draw_shape(t,color,side_length,sides,x,y)

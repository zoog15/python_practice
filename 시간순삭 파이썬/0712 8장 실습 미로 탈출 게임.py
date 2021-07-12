import turtle

def draw_maze(x,y) : #미로 그리기
    for i in range(2) :
        t.penup()
        if i==1 :
            t.goto(x+100,y+100)
        else :
            t.goto(x,y)
        t.pendown()
        t.forward(300)
        t.right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)

def turn_left() :
    t.left(10)
    t.forward(10)

def turn_right() :
    t.right(10)
    t.forward(10)

t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.speed(0)

draw_maze(-300,200)
screen.onkey(turn_left,"Left") #키보드 왼쪽 누르면 turn_left 함수 호출
screen.onkey(turn_right,"Right")#키보드 오른쪽 누르면 turn_right 함수 호출

t.penup();
t.goto(-300,250)
t.pendown()
screen.listen() #프로그램 활성화
screen.mainloop() #프로그램이 계속 동작하는 상태를 유지, 사용자가 직접 끄기전까지

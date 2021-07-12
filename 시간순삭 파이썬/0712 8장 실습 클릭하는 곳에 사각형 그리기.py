import turtle

t = turtle.Turtle()

def square(length) : #사각형을 그리는 함수
    for i in range(4) :
        t.forward(length)
        t.left(90)

def drawit(x,y): #x,y좌표를 중심점으로 초록색으로 꽉찬 사각형 그리기
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill() #색채우기 시작
    t.color("green") #색지정
    square(50)
    t.end_fill() #색채우기 


s = turtle.Screen() # 현재 터틀 그래픽이 그려지는 화면을 s라고 부를수있게 생성
s.onscreenclick(drawit) # s화면에 마우스가 클릭되면 drawit이 실행


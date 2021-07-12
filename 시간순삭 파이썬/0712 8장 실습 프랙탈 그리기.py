import turtle

def tree(length) :
    if length > 5 : #length가 5보다 클동안 tree함수 순환호출
        t.forward(length)
        t.right(20)
        tree(length - 15)
        t.left(40)
        tree(length - 15)
        t.right(20) 
        t.backward(length) # length만큼 뒤로 간다. 제자리로 돌아옴.

t = turtle.Turtle()
t.left(90)

t.color("green")
t.speed(1) # 속도를 제일 느리
tree(90)

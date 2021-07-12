import turtle

t = turtle.Turtle()

def n_polygon(n,length):
    for i in range(n) :
        t.forward(length)
        t.left(360/n)

length = int(input("한변의 길이를 입력하시오."))
n = int(input("꼭짓점의 갯수를 입력하시오."))

for i in range(10) :
    t.left(20)
    n_polygon(n,length)

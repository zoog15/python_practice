import turtle

t = turtle.Turtle()

t.speed(0) # 0으로하면 스피드가 최대
t.width(3) # 그리는 선의 두께는 3

length = 10 # 처음 길이는 10

colors = ["red","purple","blue","green","yellow","orange"]

while length < 500 : # 길이가 500을 넘기 전까지
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length += 5

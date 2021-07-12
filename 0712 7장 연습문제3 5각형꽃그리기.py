import turtle

t = turtle.Turtle()

color = ["blue","yellow","green","orange","red"]

for j in color :
    t.color(j)
    for i in range(5) :
        t.forward(100)
        t.right(72)
    t.right(72)

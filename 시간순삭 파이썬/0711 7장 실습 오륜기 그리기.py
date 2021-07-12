import turtle

t = turtle.Turtle()

positions = [[0,0,"green"],[-120,0,"yellow"],[60,60,"red"],[-60,60,"black"],[-180,60,"blue"]]

for x,y,c in positions :
    t.penup()
    t.goto(x,y)
    t.color(c,c)
    t.pendown()
    t.circle(60)
    

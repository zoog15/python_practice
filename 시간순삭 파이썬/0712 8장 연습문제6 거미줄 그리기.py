import turtle
t= turtle.Turtle()
t.shape("turtle")
t.speed(0)

def draw_line():
    t.forward(100)
    t.backward(100)

for i in range(12) :
    draw_line()
    t.right(30)
   
    

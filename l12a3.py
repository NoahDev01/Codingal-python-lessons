import turtle
turtle.Screen().bgcolor("red")
t=turtle.Turtle()
s=0
while True:
    for i in range(4):
        t.forward(s+1)
        t.left(90)
        s=s-5  
    s=s+1

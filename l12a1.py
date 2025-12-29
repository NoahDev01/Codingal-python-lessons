import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400)
t=turtle.Turtle()
n=6
l=70
a=360/n
for i in range(n):
    t.forward(l)
    t.right(a)
turtle.done()    
    


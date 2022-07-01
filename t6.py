from turtle import *

speed('slowest')
bgcolor('black')
pencolor('white')

penup()
setpos(-200,200)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)

mainloop()
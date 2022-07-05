from turtle import *

side = 6

for i in range(side):
    dot(100,'red')
    fd(100)
    pensize(side*i)
    lt(360/side)
    dot(90,'red')
    circle(90,180)
    
mainloop()
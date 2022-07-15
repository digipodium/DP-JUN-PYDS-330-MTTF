from turtle import *
speed('fastest')
colors = ['red', 'blue', 'green', 'pink', 'purple', 'orange']

s = len(colors)
for i in range(500):
    c = colors[i % s]
    pencolor(c)
    forward(i+25)
    left(360/s)
    for j in range(s):
        forward(i+25)
        left(60) 
    


    
mainloop()
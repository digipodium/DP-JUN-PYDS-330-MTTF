from turtle import *  # import all the functions from turtle module

t1 = Turtle()      # create a turtle object
t2 = Turtle()      # create a turtle object
t3 = Turtle()      # create a turtle object
t1.pencolor('red')  # set the color of the pen
t2.pencolor('blue') # set the color of the pen
t3.pencolor('green') # set the color of the pen
t1.speed('slow')
left(-90)
forward(200)
t1.forward(100)    # t1 moves forward 100 units
t2.backward(100)   # t2 moves backward 100 units
t3.left(90)        # t3 turns left 90 degrees
t3.forward(100)    # t3 moves forward 100 units

mainloop()          # keep the window open
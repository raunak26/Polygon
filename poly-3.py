# poly-3.py
# Raunak Anand
# This program reads an integer n
# and draws a regular polygon with n sides

import turtle               # allows us to use turtles

# size of the rectangle's sides
side = 50

# set up the drawing
# window stuff first

window = turtle.Screen()        # draw the window for the picture
poly = turtle.Turtle()          # create a turtle, called "poly"
try:
    n = int(input("How many sides would you like your polygon to have?: "))
    poly.shape("turtle")
    poly.speed(3)                # a turtle is slow (10 fastest, 1 slowest)
    poly.color("red")          # make colour of the pen white
    poly.pensize(2)              # make the lines 2 pixels

    # draw the box
    for i in range(int(n)):
        poly.forward(side)             # tell box to move forward some
        poly.right(360/int(n))               # tell box to turn right

except:
    print("Please print an integer")

window.mainloop()               # wait until the user closes the window

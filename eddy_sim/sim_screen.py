#!/usr/bin/python3
import rospy, turtle, sys, os,  math, random

# THE SCREEN

# screen setup
win = turtle.Screen()
win.setup(800,600)
win.title("eddy_sim")
# win.register_shape('lake.gif')
# win.register_shape('eddy.gif')
win.tracer(6)


# eddy on the screen
# win.register_shape('eddy.obj')
  eddy= turtle.Turtle()
# eddy.shape('eddy.obj')
# eddy.penup()
# eddy.goto(-200, 200)
# eddy.hideturtle()

# putting weeds on the screen
weedSections = 3
weeds = []

for count in range(weedSections):
    weeds.append(turtle.Turtle())
    weeds[count].color("green")
    weeds[count].shape("circle")
    weeds[count].penup()
    weeds[count].setposition(random.randint(-215, 215), random.randint(-215, 215))

# keys
turtle.listen()
turtle.onkey(changeScreen, "Return")

vel = 1

def moveforward():
    player1.forward(20)

def turnleft():
    player1.left(90)

def turnright():
    player1.right(90)

turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(moveforward, "Up")

while True:
    # move car
    eddy.penup()
    eddy.forward(speed)
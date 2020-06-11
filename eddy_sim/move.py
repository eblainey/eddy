#!/usr/bin/python3
import rospy, turtle, sys, os,  math, random

def moveforward():
    player1.forward(20)


# turnleft
# turns player 90 degrees to the left
# @param: none
# @return: player1X, player1Y
def turnleft():
    player1.left(90)


# turnright
# turns player 90 degrees to the right
# @param: none
# @return: player1X, player1Y
def turnright():
    player1.right(90)


# keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(moveforward, "Up")

#!/usr/bin/python3



# updates the location of the robot by taking the current position of the robot (x,y,theta)
# and moving it to (x+dt*linearx * cos(theta), y+dt*linearx*sin(theta), theta+dt angularz)


# It publishes this as a Pose

# It listens to a message of type Pose (called set_pose) that sets the pose.


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
# eddy= turtle.Turtle()
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
# imports
import rospy
from eddy_sim.msg import Pose
from geometry_msgs.msg import Twist

# listens to
# twist messages where linear y and z are 0 and linear x is m/2 and is the forward velocity of Eddy.
# Angular x and y are zero and angular z is rotation of eddy in radians/s counter clockwise.


# updates the location of the robot by taking the current position of the robot (x,y,theta)
# and moving it to (x+dt*linearx * cos(theta), y+dt*linearx*sin(theta), theta+dt angularz)


# It publishes this as a Pose

# It listens to a message of type Pose (called set_pose) that sets the pose.


#node

if __name__ = '__main__':
    try:
        rospy.init_node('eddy_sim')


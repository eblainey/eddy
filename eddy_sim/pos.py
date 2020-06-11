#!/usr/bin/ python3
import rospy
from eddy_sim.msg import Pose
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

pose = Pose()
twist = Twist()

def pos_cb(msg):
    pose = msg.pose.pose # (x,y,theta)

    twist.linear.x = pose[0]
    twist.angular.z = pose[2]

# END ALL
# listens to
# twist messages where linear y and z are 0 and linear x is m/2 and is the forward velocity of Eddy.
# Angular x and y are zero and angular z is rotation of eddy in radians/s counter clockwise.

def get_messages():


# updates the location of the robot by taking the current position of the robot (x,y,theta)
# and moving it to (x+dt*linear.x * cos(theta), y+dt*linearx*sin(theta), theta+dt angularz)
def update_location():





# It publishes this as a Pose

# It listens to a message of type Pose (called set_pose) that sets the pose.




def main():
        rospy.init_node('eddy_sim') #node
        rospy.Subscriber('eddy/sonar/cmd_vel', Twist, pos_cb) #sub to topic

        rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass


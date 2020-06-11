#!/usr/bin/python3

import time, rospy, roslib, rosbag sys, numpy, os
import unpack_bytearray
import matplotlib.pyplot as plt
from struct import Struct
from argparse import ArgumentParser
from brping import PingParser, Ping1d
from rosgraph_msgs.msgs import Log, Clock

###PARSE
parser = argparse.ArgumentParser()
parser.add_argument('--device', action="store", required=False, type=str, help="Ping device port. E.g: /dev/ttyUSB0")
parser.add_argument('--baudrate', action="store", type=int, default=115200, help="Ping device baudrate. E.g: 115200")
args = parser.parse_args()

###GET THE PING
ping = Ping1D()

if args.device is not None:
    ping.connect_serial(args.device, args.baudrate)

if ping.initialize() is False:
    rospy.logerror("Failed to initialize Ping!")

    #GET from ROSBAG

###Config Data


###READ with a loop
    def sonar_data():
        rate = rospy.Rate(10) #10 hz

        while not rospy.is_shutdown():
            time = rospy.get_time()
            data = ping.get_profile()
            f = open('profile_dict.b', 'wb')
            distance = data["distance"] #mm
            transmit_duration = data["transmit_duration"]
            confidence = data["confidence"] #%
            profile_data = data["profile_data"] #uint8[]
            rate.sleep()
            pass


















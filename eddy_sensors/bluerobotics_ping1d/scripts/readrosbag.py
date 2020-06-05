#!/usr/bin/env python3

import rosbag
bag = rosbag.Bag('eddy-realpooldata-2020-05-2-7-05-40-49.bag')
for topic, msg, t in bag.read_messages(topics=['/eddy/sonar/distance', '/eddy/sonar/history','/eddy/sonar/profile','/image_view/output']):
    print(msg)
bag.close()
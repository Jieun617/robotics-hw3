#!/usr/bin/env python
import rospy
from common_msgs.msg import common_msgs

def callback(msg):
    print "subscribe:", msg.timestamp.secs%100, msg.vector.x, msg.vector.y, msg.vector.z

rospy.init_node('algorithm_subscriber')
sub = rospy.Subscriber('custom_msg', common_msgs, callback)
rospy.spin()

#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3
from common_msgs.msg import common_msgs

rospy.init_node('sensor_publisher')
pub = rospy.Publisher('sensor_msg', common_msgs, queue_size=1)
msg = common_msgs()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.vector = Vector3(x=second%4, y=second%7, z=second%5)
    pub.publish(msg)
    print "publish:", msg.timestamp.secs%100, msg.vector.x, msg.vector.y, msg.vector.z
    rate.sleep()


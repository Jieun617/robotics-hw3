#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3
from common_msgs.msg import common_msgs
from common_msgs.srv import AddTwoNum, AddTwoNumRequest


rospy.init_node('sensor_service')
pub = rospy.Publisher('custom_msg', common_msgs, queue_size=1)
rospy.wait_for_service('add_two_number')
requester = rospy.ServiceProxy('add_two_number', AddTwoNum)
print("requester type:", type(requester), ", callable?", callable(requester))
msg = common_msgs()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.vector = Vector3(x=second%4, y=second%7, z=second%5)
    pub.publish(msg)
    print("publish:", msg.timestamp.secs%100, msg.vector.x, msg.vector.y, msg.vector.z)
    if second % 20 == 0:
        req = AddTwoNumRequest(a=msg.vector.x, b= msg.vector.y*2, c= msg.vector.z*2)
        res = requester(req)
	print(second%100, "request:", req.a, req.b, req.c, " response:", res.sum)
    rate.sleep()

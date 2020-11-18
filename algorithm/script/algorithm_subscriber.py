#!/usr/bin/env python
import rospy
from common_msgs.msg import common_msgs
from common_msgs.srv import AddTwoNum, AddTwoNumResponse


def callback(msg):
    print("subscribe:", msg.timestamp.secs%100, msg.vector.x, msg.vector.y, msg.vector.z)

def service_callback(request):
    response = AddTwoNumResponse(sum=request.a + request.b + request.c)
    print("request data:", request.a, request.b, request.c, " response:", response.sum)
    return response



rospy.init_node('algorithm_service')
sub = rospy.Subscriber('custom_msg', common_msgs, callback)
service = rospy.Service('add_two_number', AddTwoNum, service_callback)
rospy.spin()

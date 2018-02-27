#!/usr/bin/env python

import rospy
from std.msgs.msg import String

class Motor_Node:

    def __init__(self):
        self.outmsg = 'hello, world' #TODO encoder/decoder info
        self.pubsub()

    def get_commands(self, inmsg):
        rospy.loginfo(rospy.get_caller_id() + ' ' + data.data)
        #TODO - actually process motor commands

    def pubsub(self):
        pub = rospy.Publisher('arm_motion', String, queue_size=10)
        rospy.init_node('base_motors', anonymous=True)
        rospy.Subscriber('joy', String, get_commands)
        while not rospy.is_shutdown():
            str = "hello" #TODO - add encoder/decoder info here
            rospy.loginfo(str) #for debugging purposes
            pub.publish(str)
            rate.sleep()
            rospy.spin()

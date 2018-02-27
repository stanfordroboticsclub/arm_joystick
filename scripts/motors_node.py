#!/usr/bin/env python

import rospy
from std.msgs.msg import String

class Motor_Node:

    def __init__(self):
        self.outmsg = 'hello, world' #TODO encoder/decoder info
        self.uart = '/dev/ttyS0'
        self.baud = 115200
        
        self.tur_elb = Roboclaw(self.uart, self.baud)
        self.wrist = Roboclaw(self.uart, self.baud)
        self.shoulder = Roboclaw(self.uart, self.baud)

        self.tur_elb.Open()
        self.wrist.Open()
        self.shoulder.Open()
        
        self.TE_ADDR = 0x80
        self.WR_ADDR = 0X81
        self.SH_ADDR = 0x82

        self.pubsub()

    def get_commands(self, inmsg):
        rospy.loginfo(rospy.get_caller_id() + ' ' + data.data)
        #TODO - actually process motor commands

    def update_info(self): #TODO actually make readable + useful updates
        enc1 = rc.ReadEncM1(address)
	enc2 = rc.ReadEncM2(address)
	speed1 = rc.ReadSpeedM1(address)
	speed2 = rc.ReadSpeedM2(address)

	print("Encoder1:"),
	if(enc1[0]==1):
		print enc1[1],
		print format(enc1[2],'02x'),
	else:
		print "failed",
	print "Encoder2:",
	if(enc2[0]==1):
		print enc2[1],
		print format(enc2[2],'02x'),
	else:
		print "failed " ,
	print "Speed1:",
	if(speed1[0]):
		print speed1[1],
	else:
		print "failed",
	print("Speed2:"),
	if(speed2[0]):
		print speed2[1]
	else:
		print "failed "


    def pubsub(self):
        self.pub = rospy.Publisher('arm_motion', String, queue_size=10)
        rospy.init_node('base_motors', anonymous=True)
        self.sub = rospy.Subscriber('joy', String, get_commands)
        while not rospy.is_shutdown():
            str = self.update_info()
            rospy.loginfo(str) #for debugging purposes
            pub.publish(str)
            rate.sleep()
            rospy.spin()

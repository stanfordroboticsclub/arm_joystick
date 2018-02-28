#!/usr/bin/env python

import rospy
from std.msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class Motor_Node:

    def __init__(self):
        self.outmsg = 'empty'
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

        data.axes #float-32[]
        data.buttons #int-32[]
        #TODO - actually process joystick/motor commands
        #call move_motors

        self.update_info()
        
    def move_motors(self, command, val=0):
        {
            0: self.tur_elb.ForwardM1(self.TE_ADDR, val),
            1: self.tur_elb.BackwardM1(self.TE_ADDR, val),
            2: self.tur_elb.ForwardM2(self.TE_ADDR, val),
            3: self.tur_elb.BackwardM2(self.TE_ADDR, val),
            4: self.wrist.ForwardM1(self.WR_ADDR, val),
            5: self.wrist.BackwardM1(self.WR_ADDR, val),
            6: self.wrist.ForwardM2(self.WR_ADDR, val),
            7: self.wrist.BackwardM2(self.WR_ADDR, val),
            8: self.shoulder.ForwardM1(self.SH_ADDR, val),
            9: self.shoulder.BackwardM1(self.SH_ADDR, val),
        }[command]

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

        #rospy.loginfo(str) #for debugging purposes
        self.pub.publish(str)

    def pubsub(self):
        self.pub = rospy.Publisher('arm_motion', String, queue_size=10)
        rospy.Subscriber('joy', Joy, get_commands)
        rospy.init_node('base_motors', anonymous=True)
        rospy.spin()

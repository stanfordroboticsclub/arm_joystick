#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from roboclaw import Roboclaw

class Motor_Node:

    def __init__(self):
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

        self.HL = 0
        self.VL = 1
        self.HR = 2
        self.HL = 3
        
        self.pubsub()

    def get_commands(self, inmsg):
        rospy.loginfo(rospy.get_caller_id() + ' ' + data.data)

        # turret control
        if (data.buttons[7]): # right forward button hopefully
            self.move_motors(0, val=(64 + int(data.axes[self.HR]/2)))
        # wrist control
        else:
            self.move_motors(2, val=(64 + int(data.axes[self.HR]/2)))
            self.move_motors(3, val=(64 + int(data.axes[self.VR]/2)))

        # turret control
        if (data.buttons[6]): # left forward button hopefully
            self.move_motors(0, val=(64 + int(data.axes[self.HL]/2)))
        # shoulder and elbow control
        else:
            self.move_motors(1, val=(64 + int(data.axes[self.HL]/2)))
            self.move_motors(4, val=(64 + int(data.axes[self.VL]/2)))
            
        self.update_info()
        
    def move_motors(self, command, val=0):
        {
            0: self.tur_elb.ForwardBackwardM1(self.TE_ADDR, val),
            1: self.tur_elb.ForwardBackwardM2(self.TE_ADDR, val),
            2: self.wrist.ForwardBackwardM1(self.WR_ADDR, val),
            3: self.wrist.ForwardBackwardM2(self.WR_ADDR, val),
            4: self.shoulder.ForwardBackwardM1(self.SH_ADDR, val),
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
        rospy.Subscriber('joy', Joy, self.get_commands)
        rospy.init_node('base_motors', anonymous=True)
        rospy.spin()

if __name__ == '__main__':
    m = Motor_Node()

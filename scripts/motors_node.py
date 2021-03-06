#!/usr/bin/env python

import rospy
import numpy as np
import struct
from math import pi
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from roboclaw import Roboclaw

TAU = 2 * pi
TE_ADDR = 0X80
WR_ADDR = 0X81
SH_ADDR = 0X82

HL = 0
VL = 1
HR = 2
VR = 3

#TODO - ACTUALLY FIGURE OUT VALUES
#TURRET, ELBOW, WRIST1, WRIST2, SHOULDER
TICKS_PER_REV = np.array([60000, 60000, 60000, 60000, 60000])

def init(uart='/dev/TTYTHS0', baud=115200):        
    global rc
    rc = Roboclaw(uart, baud)
    rc.Open()
    
    global pub
    pub = rospy.Publisher('arm_motion', String, queue_size=10)
    rospy.Subscriber('joy', Joy, manual_control)
    rospy.init_node('base_motors', anonymous=True)
    rospy.spin()

def manual_control(data):
    values = np.empty(4, dtype=np.int8)
    print(values)
    for i in xrange(4):
        values[i] = int(data.axes[i] * 63 + 64)
        
    # turret control
    if (data.buttons[5]): # RB
        rc.ForwardBackwardM1(TE_ADDR, values[HR])
    # wrist control
    else:
        rc.ForwardBackwardM1(WR_ADDR, values[HR])
        rc.ForwardBackwardM2(WR_ADDR, values[VR])
            
    # turret control
    if (data.buttons[4]): # LB
        rc.ForwardBackwardM1(TE_ADDR, values[HL])
    # shoulder and elbow control
    else:
        rc.ForwardBackwardM2(TE_ADDR, values[HL])
        rc.ForwardBackwardM1(SH_ADDR, values[VL])

    update_info()

# turret, elbow, wrist1, wrist2, shoulder
# angular displacement in signed radians
def position_control(speed, ang_disp):
    dist = np.multiply(ang_disp / TAU, TICKS_PER_REV)
    #TODO write x5 for 5 motors lol
    rc.SpeedDistanceM1(TE_ADDR, speed[0], dist[0])
    rc.SpeedDistanceM2(TE_ADDR, speed[1], dist[1])
    rc.SpeedDistanceM1(WR_ADDR, speed[2], dist[2])
    rc.SpeedDistanceM2(WR_ADDR, speed[3], dist[3])
    rc.SpeedDistanceM1(SH_ADDR, speed[4], dist[4])
        
def update_info(): #TODO actually make readable + useful updates
    print("doing stuff")
    enc1 = rc.ReadEncM1(TE_ADDR)
    enc2 = rc.ReadEncM2(TE_ADDR)
    print(enc1)
    print(enc2)
    """
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
    """
    str = "send something useful"
    #rospy.loginfo(str) #for debugging purposes
    pub.publish(str)
        
if __name__ == '__main__':
    init()

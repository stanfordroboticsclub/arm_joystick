from roboclaw import Roboclaw
import time

print('start')

rc = Roboclaw('/dev/ttyTHS0', 115200)
rc.Open()
addr = 129
"""
for i in xrange(128):
    rc.ForwardM1(addr, i)
"""
print('why')

#Linux comport name
roboclaw = Roboclaw('/dev/ttyTHS0', 115200)
roboclaw.Open()
address = 0x81
if roboclaw.ForwardMixed(address, 100):
    print("why aren't the motors moving?!")

print(roboclaw.ReadTemp(address))
print(roboclaw.ReadTemp2(address))
time.sleep(2)
if roboclaw.ForwardBackwardM1(address, 96):
    print("m1 should move")
if roboclaw.ForwardBackwardM2(address, 32):
    print("m2 should back")

print(roboclaw.ReadEncoderModes(address))
time.sleep(2)
if roboclaw.ForwardM2(address, 64):
    print("m2 should forward")
if roboclaw.BackwardM1(address, 64):
    print("m1 should back")

time.sleep(2)
roboclaw.ForwardM1(address, 0)
roboclaw.ForwardM2(address, 0)

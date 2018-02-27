from roboclaw import Roboclaw
import time

#Linux comport name
roboclaw = Roboclaw("/dev/ttyS0",115200)
roboclaw.Open()
address = 0x80
roboclaw.ForwardM1(address, 64)
roboclaw.BackwardM2(address, 64)

time.sleep(2)
roboclaw.ForwardM2(address, 64)
roboclaw.BackwardM1(address, 64)

time.sleep(2)
roboclaw.ForwardM1(address, 0)
roboclaw.ForwardM2(address, 0)

import time
import sys
from dorna2 import Dorna

r = Dorna()
r.connect("192.168.88.252")

def exitHandler():
    print("Exiting gracefully")
    r.halt()
    r.close()
    sys.exit(0)


try:
    while True:
        time.sleep(10)
        # status = r.jmove(rel=1, j0=-20, vel=25, accel=50, jerk=250)
        # print(status)
        # status = r.jmove(rel=1, j0=-20)
        # print(status)
except KeyboardInterrupt:
    exitHandler()

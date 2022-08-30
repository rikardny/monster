from helper import *

r = Robot()

status = r.jmove(0,35,-125,0,0)
print(status)
status = r.jmove(0,45,-135,0,0)
print(status)

r.stop()

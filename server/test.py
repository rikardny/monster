import sys
from dorna2 import Dorna

r = Dorna()
r.connect("192.168.88.252")

try:
    while True:
        status = r.jmove(rel=1, j0=20)
        print(status)
        status = r.jmove(rel=1, j0=-20)
        print(status)
except KeyboardInterrupt:
    print("Exiting gracefully")
    r.halt()
    r.close()
    sys.exit(0)

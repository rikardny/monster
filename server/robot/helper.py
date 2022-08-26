from dorna2 import dorna
from time import sleep
import json

class Robot:
    # Constructor, import ip adresses and port from json
    def __init__(self):
        with open("config.json") as json_file:
            arg = json.load(json_file)

        self.robot = dorna()
        self.robot.connect(arg["ip"], arg["port"])

    # Robot joint move, simplified into one line
    def jmove(self, j0, j1, j2, j3, j4):
        vel, accel, jerk = 250, 3000, 500

        arg = {"cmd": "jmove", "rel":0, "id": self.robot.rand_id(), \
                "j0": j0, "j1": j1, "j2": j2, "j3": j3, "j4": j4,
                "vel": vel, "accel": accel, "jerk": jerk}
        trk = self.robot.play(True, **arg)
        trk.complete()


    # Robot linear move, simplified into one line
    def lmove(self, x, y, z, a, b):
        vel, accel, jerk = 500, 1500, 500

        arg = {"cmd": "lmove", "rel":0, "id": self.robot.rand_id(), \
                "x": x, "y": y, "z": z, "a": a, "b": b, \
                "vel": vel, "accel": accel, "jerk": jerk}
        trk = self.robot.play(True, **arg)
        trk.complete()


    # Robot joint move relative to current position, simplified into one line
    def rel_jmove(self, j0, j1, j2, j3, j4):
        vel, accel, jerk = 10, 500, 2500

        arg = {"cmd": "jmove", "rel":1, "id": self.robot.rand_id(), \
                "j0": j0, "j1": j1, "j2": j2, "j3": j3, "j4": j4,
                "vel": vel, "accel": accel, "jerk": jerk}
        trk = self.robot.play(True, **arg)
        trk.complete()


    # Robot linear move relative to current position, simplified into one line
    def rel_lmove(self, x, y, z, a, b):
        vel, accel, jerk = 10, 500, 2500

        arg = {"cmd": "lmove", "rel":1, "id": self.robot.rand_id(), \
                "x": x, "y": y, "z": z, "a": a, "b": b, \
                "vel": vel, "accel": accel, "jerk": jerk}
        trk = self.robot.play(True, **arg)
        trk.complete()

    # Grip microplate
    def grip(self):
        arg = {"cmd": "pwm", "id": self.robot.rand_id(), \
                "pwm0": 1, "duty0": 8.0, "freq0": 50}
        trk = self.robot.play(True, **arg)
        sleep(0.4)
        trk.complete()


    # Release microplate
    def release(self):
        arg = {"cmd": "pwm", "id": self.robot.rand_id(), \
                "pwm0": 1, "duty0": 9, "freq0": 50}
        trk = self.robot.play(True, **arg)
        sleep(0.4)
        trk.complete()

    # Fully open gripper
    def open(self):
        arg = {"cmd": "pwm", "id": self.robot.rand_id(), \
                "pwm0": 1, "duty0": 12.5, "freq0": 50}
        trk = self.robot.play(True, **arg)
        sleep(0.4)
        trk.complete()


    def stop(self):
        self.robot.close()

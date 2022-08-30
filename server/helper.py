from dorna2 import Dorna
from time import sleep
import json

class Robot:
    # Constructor, import ip adresses and port from json
    def __init__(self):
        with open("config.json") as json_file:
            arg = json.load(json_file)

        self.robot = Dorna()
        self.robot.connect(arg["ip"], arg["port"])

    def activate(self):
        if self.robot.get_motor() == 0:
            status = self.robot.set_motor(1)
        else:
            status = "Motors are already on"
        return status

    # Robot joint move, simplified into one line
    def jmove(self, j0, j1, j2, j3, j4):
        vel, accel, jerk = 5, 500, 2500

        arg = {"cmd": "jmove", "rel":0, "id": self.robot.rand_id(), \
                "j0": j0, "j1": j1, "j2": j2, "j3": j3, "j4": j4,
                "vel": vel, "accel": accel, "jerk": jerk}
        status = self.robot.play(True, **arg)
        return status


    # Robot linear move, simplified into one line
    def lmove(self, x, y, z, a, b):
        vel, accel, jerk = 50, 1000, 5000

        arg = {"cmd": "lmove", "rel":0, "id": self.robot.rand_id(), \
                "x": x, "y": y, "z": z, "a": a, "b": b, \
                "vel": vel, "accel": accel, "jerk": jerk}
        status = self.robot.play(True, **arg)
        return status


    # Robot joint move relative to current position, simplified into one line
    def rel_jmove(self, j0, j1, j2, j3, j4):
        vel, accel, jerk = 10, 500, 2500

        arg = {"cmd": "jmove", "rel":1, "id": self.robot.rand_id(), \
                "j0": j0, "j1": j1, "j2": j2, "j3": j3, "j4": j4,
                "vel": vel, "accel": accel, "jerk": jerk}
        status = self.robot.play(True, **arg)
        return status


    # Robot linear move relative to current position, simplified into one line
    def rel_lmove(self, x, y, z, a, b):
        vel, accel, jerk = 10, 500, 2500

        arg = {"cmd": "lmove", "rel":1, "id": self.robot.rand_id(), \
                "x": x, "y": y, "z": z, "a": a, "b": b, \
                "vel": vel, "accel": accel, "jerk": jerk}
        status = self.robot.play(True, **arg)
        return status


    # Grip microplate
    def grip(self):
        arg = {"cmd": "pwm", "id": self.robot.rand_id(), \
                "pwm0": 1, "duty0": 8.0, "freq0": 50}
        status = self.robot.play(True, **arg)
        sleep(0.4)
        return status

    # Release microplate
    def release(self):
        arg = {"cmd": "pwm", "id": self.robot.rand_id(), \
                "pwm0": 1, "duty0": 9, "freq0": 50}
        status = self.robot.play(True, **arg)
        sleep(0.4)
        return status

    # Fully open gripper
    def open(self):
        arg = {"cmd": "pwm", "id": self.robot.rand_id(), \
                "pwm0": 1, "duty0": 12.5, "freq0": 50}
        status = self.robot.play(True, **arg)
        sleep(0.4)
        return status

    def halt(self):
        self.robot.halt(accel=None)

    def stop(self):
        self.robot.close()

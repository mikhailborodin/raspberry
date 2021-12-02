from time import sleep
import troykahat


ap = troykahat.analog_io()


class Device:
    PIN: int


class Sensor(Device):
    PIN = 3

    def __init__(self):
        ap.pinMode(self.PIN, ap.INPUT)

    def read(self):
        return ap.analogRead(self.PIN) * 100

    def turn_off(self):
        ap.digitalWrite(self.PIN, False)


class LED(Device):
    PIN = 7

    def __init__(self):
        ap.pinMode(self.PIN, ap.OUTPUT)

    def blink(self):
        ap.analogWrite(self.PIN, 0.25)
        sleep(0.2)
        ap.analogWrite(self.PIN, 0)

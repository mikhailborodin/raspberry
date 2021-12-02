import troykahat
from prometheus_client import Gauge, start_http_server
from time import sleep

ap = troykahat.analog_io()
gh = Gauge('humidity_ground', 'Humidity ground')


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


if __name__ == '__main__':
    start_http_server(8000)
    sensor = Sensor()
    led = LED()
    while True:
        value = sensor.read()
        gh.set(value)
        if value < 0.1:
            led.blink()
        sensor.turn_off()
        sleep(30)

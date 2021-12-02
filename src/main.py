from prometheus_client import Gauge, start_http_server
from time import sleep
from devices import LED, Sensor

DEFAULT_SLEEP_TIME = 60
CRITICAL_VALUE = 0.1

if __name__ == '__main__':
    gh = Gauge('humidity_ground', 'Humidity ground')
    start_http_server(8000)
    sensor = Sensor()
    led = LED()
    while True:
        value = sensor.read()
        gh.set(value)
        if value < CRITICAL_VALUE:
            led.blink()
        sensor.turn_off()
        sleep(DEFAULT_SLEEP_TIME)

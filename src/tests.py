from main import Sensor


def test_sensor():
    sensor = Sensor()
    value = sensor.read()
    assert isinstance(value, float)


test_sensor()

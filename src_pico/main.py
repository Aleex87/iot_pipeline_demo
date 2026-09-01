from time import sleep
from wifi import connect_wifi
from machine import Pin 
from dht import DHT11

sleep(.1)

led = Pin(15, Pin.OUT)

if connect_wifi():
    led.value(1)
dht_sensor = DHT11(Pin(3)) 

while True:
    sleep(5)
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    humidity = dht_sensor.humidity()

    data={"temperature":temp, "humidity":humidity}
    print(data)
    
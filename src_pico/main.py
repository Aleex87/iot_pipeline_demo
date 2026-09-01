from time import sleep
from wifi import connect_wifi
from machine import Pin 

sleep(.1)

led = Pin(15, Pin.OUT)

if connect_wifi():
    led.value(1)
    
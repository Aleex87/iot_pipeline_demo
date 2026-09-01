from time import sleep
from wifi import connect_wifi
from machine import Pin 
from dht import DHT11
from umqtt.simple import MQTTClient
import json

sleep(0.1)

# byte rappresentation -> mosquitto needs this
TOPIC = b"home/pico/dht11"

# ipconfig from the terminal and in windows chose the ipv4 
MQTT_BROCKER = "172.18.32.1"

led = Pin(15, Pin.OUT)

if connect_wifi():
    led.value(1)
    
dht_sensor = DHT11(Pin(3)) 

def connect_mqtt():
    client = MQTTClient(client_id="pico", server=MQTT_BROCKER, port=1883)
    client.connect()
    print("Connect to MQTT")
    return client

client = connect_mqtt()

while True:
    sleep(5)
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    humidity = dht_sensor.humidity()

    data={"temperature":temp, "humidity":humidity}
    print(data)
    # dict -> 
    payload = json.dumps(data)
    client.publish(TOPIC, payload)
    sleep(1)
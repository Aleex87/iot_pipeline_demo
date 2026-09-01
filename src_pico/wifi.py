import json
import network
import rp2
import time

rp2.country("SE")

with open("wifi_credentials.json") as file:
    credentials = json.load(file)

def connect_wifi(waiting_time = 10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True) 
    wlan.connect(credentials.get("SSID"), credentials.get("PASSWORD"))

    while waiting_time > 0:
        if wlan.isconnected():
            print("congratz is connected!")
            break


        waiting_time =- 1
        print("Try to connect to the wifi")
        time.sleep(2)

    return wlan.isconnected()


print(credentials)

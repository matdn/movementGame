from machine import Pin, PWM
import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import json
import utime
# Configuration du capteur IR
sensor_pin = Pin(5, Pin.IN)  # Modifier selon votre configuration de broches

ledRed = PWM(Pin(18, mode=Pin.OUT))
ledRed.freq(1_000)
ledGreen = PWM(Pin(17, mode=Pin.OUT))
ledGreen.freq(1_000)

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi
data = { "bTrigger": 0 }

last_motion_time = 0
bTriggered = False

ssid = 'iPhone de Matis (3)'
password = 'Romanon4568'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://172.20.10.3:3000/jump"


while not wlan.isconnected():
    print("Waiting for connection")
    utime.sleep(1)
# Boucle principale
while True:
    
    if(sensor_pin.value() == 0 and not bTriggered):
        data['bTrigger'] = 1
        try:
            # debug 
            ledRed.duty_u16(0)
            ledGreen.duty_u16(20000)
            r = urequests.get(url)
            print(r)
            r.close()
        except Exception as e:
            print(e)
        data['bTrigger'] = 0
        last_motion_time = utime.ticks_ms()

        

        # trigger only one time
        bTriggered = True
    elif(sensor_pin.value() != 0 and bTriggered and utime.ticks_diff(utime.ticks_ms(), last_motion_time) < 1000):

        # debug 
        ledRed.duty_u16(20000)
        ledGreen.duty_u16(0)

        # trigger only one time
        bTriggered = False
    # Attendre un court instant avant de recommencer la boucle
    utime.sleep_ms(100)
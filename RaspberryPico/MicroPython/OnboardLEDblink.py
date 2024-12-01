# Bibliotheken laden
from machine import Pin
from time import sleep

# Initialisierung der Onboard-LED
led_onboard = Pin("LED", Pin.OUT)

# Wiederholung (Endlos-Schleife)
while True:
    # LED-Zustand wechseln (EIN/AUS)
    led_onboard.toggle()
    # 1 Sekunde warten
    sleep(1)

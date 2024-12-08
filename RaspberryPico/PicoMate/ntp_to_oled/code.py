import time
import board
import busio
import displayio
from adafruit_ssd1306 import SSD1306_I2C
import wifi
import socketpool
import adafruit_ntp
import rtc

# WLAN-Zugangsdaten
WIFI_SSID = "FRITZ!Repeater 3000"
WIFI_PASSWORD = ""

# I2C-Pins und Display-Setup
i2c = busio.I2C(scl=board.GP17, sda=board.GP16)
WIDTH = 128
HEIGHT = 32
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Verbinden mit WLAN
print("Verbinde mit WLAN...")
wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
print("Mit WLAN verbunden!")
print("IP-Adresse:", wifi.radio.ipv4_address)

# Netzwerk-Socket für NTP
pool = socketpool.SocketPool(wifi.radio)
ntp = adafruit_ntp.NTP(
    pool, server="pool.ntp.org", tz_offset=1
)  # Zeit in UTC (Offset anpassen für lokale Zeit)
rtc_clock = rtc.RTC()


def display_text(str, line):
    display.text(str, 0, (line % 8) * 8, 1, font_name="/lib/font5x8.bin")


# Zeit-Update und Ausgabe
while True:
    try:
        # Hole die aktuelle Zeit
        current_time = ntp.datetime
        rtc_clock.datetime = current_time  # Setze die Echtzeituhr

        # Formatierte Uhrzeit und Datum
        formatted_date = "{:02}.{:02}.{:04}".format(
            current_time.tm_mday, current_time.tm_mon, current_time.tm_year
        )
        formatted_time = "{:02}:{:02}:{:02}".format(
            current_time.tm_hour, current_time.tm_min, current_time.tm_sec
        )

        print("Aktuelle Zeit:", formatted_time)

        # Display aktualisieren
        display.fill(0)  # Display löschen
        display.text("Datum:", 0, 0, 1, font_name="/lib/font5x8.bin")
        display.text(formatted_date, 0, 8, 1, font_name="/lib/font5x8.bin")
        display.text("Uhrzeit:", 0, 16, 1, font_name="/lib/font5x8.bin")
        display.text(formatted_time, 0, 24, 1, font_name="/lib/font5x8.bin")
        display.show()

        # Warte eine Sekunde
        time.sleep(1)
    except Exception as e:
        print("Fehler:", e)
        time.sleep(5)

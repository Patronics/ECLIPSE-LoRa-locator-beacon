#https://learn.adafruit.com/lora-and-lorawan-radio-for-raspberry-pi/raspberry-pi-wiring
#sudo pip3 install adafruit-circuitpython-rfm9x

import time
import RPi.GPIO as GPIO
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
import adafruit_rfm9x

# Configure RFM9x LoRa Radio

CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

GPIO.setmode(GPIO.BCM)

rled=19
bled=26
GPIO.setup(rled, GPIO.OUT);
GPIO.setup(bled, GPIO.OUT);

try:
    rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
    print('RFM9x: Detected')
except RuntimeError as error:
    # Thrown on version mismatch
    
    print('RFM9x Error: ', error)
while True:
    packet=None
    packet=rfm9x.receive()
    if packet is None:
        print("waiting for packet")
        GPIO.output(rled, GPIO.HIGH)
        GPIO.output(bled, GPIO.LOW)
    else:
        prev_packet=packet
        GPIO.output(rled, GPIO.LOW)
        GPIO.output(bled, GPIO.HIGH)
        packet_text=str(prev_packet, "utf-8")
        print("bbbbbbbb")
        print(str(len(packet_text))+"\n")
        print("aaaaa")
        print(str(rfm9x.last_rssi)) 
        #reply=bytes("Bruh","utf-8")
        #rfm9x.send(reply)
    time.sleep(0.1)
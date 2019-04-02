import RPi.GPIO as GPIO
from Keypad import Keypad
import time
import spidev


GPIO.setmode(GPIO.BCM)

kp = Keypad()


while True:
    button = kp.getKey()
    if button != None:
        print("button pressed: " + button)
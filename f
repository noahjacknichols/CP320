#!/usr/bin/python
# Terry Sturtevant, May 10, 2017
import RPi.GPIO as GPIO
import time
import spidev
from keypad import Keypad

GPIO.setmode(GPIO.BCM)
stepper_pins=[18,23,24,25]
keypad_input_pins = [17, 27] #GPIO pin 17, 27 is for row 1 and 2 respectively
keypad_output_pins = [20, 21] #GPIO pin 20, 21 is for column 1 and 3 respectively
led_output_pin = [5] #GPIO 5 corresponds to the LED

GPIO.setup(stepper_pins,GPIO.OUT)
GPIO.setup(keypad_input_pins, GPIO.IN)
GPIO.setup(keypad_output_pins, GPIO.OUT)

stepper_sequence=[]
stepper_sequence.append([GPIO.HIGH, GPIO.LOW, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.HIGH, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.HIGH,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.LOW,GPIO.HIGH])
degree = 2048/360
count = 0
flag = -1
distArray = []
#rotation = float(input("degree:")) //dont need this anymore
#inp = int(rotation * degree)
kp = Keypad()

def infrared_function():
	adc_channel=0
	spi=spidev.SpiDev()
	spi.open(0,0)
	spi.max_speed_hz = 5000

	try:
		adc=spi.xfer2([1,(8+adc_channel)<<4,0])
		data=((adc[1]&3)<<8) +adc[2]
		data_scale=(data*3.3)/float(1023)
		data_scale=round(data_scale,2)
		print (data_scale)
		time.sleep(2)
	except KeyboardInterrupt:
		pass
	spi.close()
	return data_scale

while True:

	try:
		x = kpgetKey()
		
		if x == 1: #auto mode
			flag = 0
		elif x == 3: #user mode
			flag = 1
		print("the flag is currently: " +str(flag))

				
		if flag == 1:
			#user solver mode
			print("user solver mode")
			try:
				while (flag == 1):
					#get flag = input of choice buttons
					#grab input on move left or right here
					x = kp.getKey()
					if x == 6:
						for row in reversed(stepper_sequence):
							print("supposed to be moving left")
							GPIO.output(stepper_pins, row)
							time.sleep(0.01)
					elif x == 4:
						for row in stepper_sequence:
							print("supposed to be moving left")
							GPIO.output(stepper_pins, row)
							time.sleep(0.01)
					if x == 1:
						flag = 0
					#update light intensity here
					distance = infrared_function()
					print("distance is: " + str(distance))
			except KeyboardInterrupt:
				print("Interrupted")		
	except KeyboardInterrupt:
		#do something here
		print("overall flag occurred")
		

GPIO.cleanup()

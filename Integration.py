#!/usr/bin/python
# Terry Sturtevant, May 10, 2017
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
stepper_pins=[18,23,24,25]

GPIO.setup(stepper_pins,GPIO.OUT)

stepper_sequence=[]
stepper_sequence.append([GPIO.HIGH, GPIO.LOW, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.HIGH, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.HIGH,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.LOW,GPIO.HIGH])
degree = 2048/360
count = 0
rotation = float(input("degree:"))
inp = int(rotation * degree)

try:
	while True:
#		for row in reversed (stepper_sequence):
		for row in stepper_sequence:
			GPIO.output(stepper_pins,row)
			time.sleep(0.01)
			count+=1
			if count == inp:
				time.sleep(2)

except KeyboardInterrupt:
	print("interrupted")
	inp = 2048 - int(inp)
	count2 = 0
	while True:
		for row in stepper_sequence:
			GPIO.output(stepper_pins, row)
			time.sleep(0.01)
			count2+=1
			if count2 == inp:
				time.sleep(10)
	time.sleep(0.5)
	pass

GPIO.cleanup()
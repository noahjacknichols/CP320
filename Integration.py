#!/usr/bin/python
# Terry Sturtevant, May 10, 2017
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
stepper_pins=[18,23,24,25]
keypad_input_pins = [17, 27] #GPIO pin 17, 27 is for row 1 and 2 respectively
keypad_output_pins = [20, 21] #GPIO pin 20, 21 is for column 1 and 3 respectively

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
inp = int(rotation * degree)
def keypad_function(row, col):
	GPIO.output(col, 1)
	int value = GPIO.input(row)
	GPIO.output(col, 0)
	return value

while True:
	if keypad_function(17, 20) == 0:
		flag = 0
	else if keypad_function(17, 21) == 0:
		flag = 1
	try:
		if flag == 0:
		# automated solver mode
			try:
				while flag == 0:
					# WHILE FLAG = 0 AND  GRAB FLAG = GPIO INPUT RIGHT AWAY
					# need function to check if any of the option buttons has been pressed
					# 
			#		for row in reversed (stepper_sequence):
					for row in stepper_sequence:
						GPIO.output(stepper_pins,row)
						time.sleep(0.01)
						count+=1
						if(count % 15 == 0):
							distArray.append(x) #we need the sensor input. save as tuple like (distance, count_val)
						if count == 360:
							#find closest object
							min = distArray[0]
							for dist in distArray:
								if dist < min:
									min = dist
							smallestObj = 0
							while(True):
								for row in stepper_sequence:
									#if smallestObj coun is equal to the mins object degree, dont. just dont.
									if(smallestObj != min[1]): 
										GPIO.output(stepper_pins, row)
										time.sleep(0.01)
										smallestObj += 1
									#set light to green or whatever
								
									
							

			except KeyboardInterrupt:
				print("interrupted")
				
		if flag == 1:
			#user solver mode
			print("user solver mode")
			try:
				while (flag == 1):
					#get flag = input of choice buttons
					#grab input on move left or right here
					input_left = 0
					input_right = 0
					if keypad_function(27, 20) == 0:
						input_left = 1
					else if keypad_function(27, 21) == 0:
						input_right = 1
					if input_left == 1:
						for row in reversed(stepper_sequence):
							GPIO.output(stepper_pins, row)
							time.sleep(0.01)
					if input_right == 1:
						for row in stepper_sequence:
							GPIO.output(stepper_pins, row)
							time.sleep(0.01)
					#update light intensity here

			except KeyboardInterrupt:
				print("Interrupted")		
	except KeyboardInterrupt:
		#do something here
		print("overall flag occurred");
GPIO.cleanup()

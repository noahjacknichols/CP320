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
flag = -1
distArray = []
#rotation = float(input("degree:")) //dont need this anymore
inp = int(rotation * degree)
while True:
	if(flag == -1):
		flag = int(input("Press one of the options button for the program"));
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
					input_left = 0 #check left button clicked here
					input_right = 0 #check right button clicked here
					if input_left:
						for row in reversed(stepper_sequence):
							GPIO.output(stepper_pins, row)
							time.sleep(0.01)
					if input_right:
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
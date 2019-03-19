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
#inp = int(rotation * degree)
def keypad_function(row, col):
    time.sleep(0.001)
	GPIO.output(col, 1)
    value = GPIO.input(row)
    print("row input = " + str(value))
	time.sleep(0.001)
    GPIO.output(col, 0)
    return value

while True:

    try:
        if keypad_function(17, 20) == 0 and keypad_function(17, 21) == 1: #auto mode
            flag = 0
        elif keypad_function(17, 21) == 0 and keypad_function(17, 20) == 1: #user mode
            flag = 1
        print("the flag is currently: " +str(flag))

                
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
                        input_right = 0 #added this just in case (testing)
                    elif keypad_function(27, 21) == 0:
                        input_right = 1
                        input_left = 0 #added this just in case
                    if input_left == 1:
                        print("moving left")
                        for row in reversed(stepper_sequence):
                            print("supposed to be moving left")
                            GPIO.output(stepper_pins, row)
                            time.sleep(0.01)
                    if input_right == 1:
                        print("moving right")
                        for row in stepper_sequence:
                            print("supposed to be moving left")
                            GPIO.output(stepper_pins, row)
                            time.sleep(0.01)
                    #update light intensity here

            except KeyboardInterrupt:
                print("Interrupted")        
    except KeyboardInterrupt:
        #do something here
        print("overall flag occurred")
GPIO.cleanup()

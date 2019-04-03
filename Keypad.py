import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
class Keypad():
    # CONSTANT VALUES FOR TELEPHONE KEYPAD
    KEYPAD = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ["*",0,"#"]
    ]

    #USED FOR PI GPIO PINS
    ROW = [17,27,13,19] #gpio pins for rows are pins 17, 27, 13, 19 (R0, R1, R2, R3 respectively)
    COLUMN = [20,16,21] #gpio pins for columns are pins 20, 16, 21 (C0, C1, C2 respectively)

    #Returns key in KEYPAD, else if no key pressed returns None
    def getKey(self):
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        RowValue = -1
        for i in range(len(self.ROW)):
            tempValue = GPIO.input(self.ROW[i])
            if tempValue == 0:
                RowValue = i
        if RowValue < 0 or RowValue > 3:
            self.exit()
            return
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.ROW[RowValue], GPIO.OUT)
        GPIO.output(self.ROW[RowValue], GPIO.HIGH)
        ColValue = -1
        for j in range(len(self.COLUMN)):
            tempValue = GPIO.input(self.COLUMN[j])
            if tempValue == 1:
                ColValue=j
        if ColValue <0 or ColValue >2:
            self.exit()
            return
        self.exit()
        return self.KEYPAD[RowValue][ColValue]

    #return boolean operator (1 OR 0) dependent on if
    #key was the expected key pressed
    def compareKey(self, expectedKey):
        keyPressed = self.getKey()
        return (1 if keyPressed == expectedKey else 0)



    def exit(self):
        for i in range(len(self.ROW)):
                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)


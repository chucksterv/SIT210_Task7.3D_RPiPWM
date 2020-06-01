import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

BUZZER= 23
GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

while True:
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.000002)
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    duration = TimeElapsed/1000000
    distanceInch = duration * 0.0133/2
    
    GPIO.output(BUZZER, True)
    time.sleep(0.05)
    GPIO.output(BUZZER, False)
    
    timer = distanceInch * 10
    timer2 = timer/1000
    time.sleep(timer2)
    
    

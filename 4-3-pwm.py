import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

p=GPIO.PWM(17,5000)
p.start(0)
try:
    while True:
        t=int(input())
        p.ChangeDutyCycle(t)
finally:
    GPIO.cleanup()
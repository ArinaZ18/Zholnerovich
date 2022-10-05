import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[26,19,13,6,5,11,9,10]
GPIO.setup(dac,GPIO.OUT)
comp=4
troyka=17
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)

def binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def adc(troyka):
    for i in range(256):
        sig=binary(i)
        GPIO.output(dac,sig)
        time.sleep(0.0001)
        value=GPIO.input(comp)
        if value == 0:
            return i


try:
    while True:
        a=adc(troyka)
        print("Напряжение на потенциометре",round((a/256)*3.3,1))
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
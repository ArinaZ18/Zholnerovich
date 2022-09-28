import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac=[26,19,13,6,5,11,9,10]
GPIO.setup(dac,GPIO.OUT)


def binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

print('Введите период:')
T=int(input())
try:
    while True:
        for i in range(255):
            GPIO.output(dac,binary(i))
            time.sleep(T/512)
        for i in range(255,-1,-1):
            GPIO.output(dac,binary(i))
            time.sleep(T/512)
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
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

def adc():
    w=[0,0,0,0,0,0,0,0]
    for i in range(8):
        w[i]=1
        GPIO.output(dac,w)
        time.sleep(0.0001)
        value=GPIO.input(comp)
        if value == 0:
            w[i]=0
        else:
            w[i]=1
    return (w[7]+w[6]*2+w[5]*2**2 + w[4]*2**3 + w[3]*2**4 +w[2]*2**5 + w[1]*2**6 + w[0]*2**7)          
try:
    while True:
        a=adc()
        print("Напряжение на потенциометре",round((a/256)*3.3,2))
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
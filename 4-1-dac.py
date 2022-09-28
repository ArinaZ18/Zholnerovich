import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac=[26,19,13,6,5,11,9,10]
GPIO.setup(dac,GPIO.OUT)
def binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]
try:
    while True:
        n=input()
        if n.isdigit():
            n=int(n)
            if n>0 and n<256:
                GPIO.output(dac,binary(n))
                p=round((3.3/256)*n,2)
                print('Напряжение на на выходе ЦАП:', p,'В')
            elif n<0:
                print('Ошибка')
                print('Введите число больше нуля')
            else:
                print('Ошибка')
                print('Введите значения не привышающее возможности 8-разрядного ЦАП')
        elif n=='q':
            break
        else:
            print('Ошибка')
            print('Введите число от 0 до 255')
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
        

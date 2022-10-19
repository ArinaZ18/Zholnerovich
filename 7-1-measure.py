import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time
GPIO.setmode(GPIO.BCM)
dac=[26,19,13,6,5,11,9,10]
leds=[24,25,8,7,12,16,20,21]
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(leds,GPIO.OUT)
comp=4
troyka=17
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)
f=[]
time1=[]
def binary(x):
    return [int(i) for i in bin(x)[2:].zfill(8)]

def adc():
    w=[0,0,0,0,0,0,0,0]
    for i in range(8):
        w[i]=1
        GPIO.output(dac,w)
        time.sleep(0.001)
        value=GPIO.input(comp)
        if value == 0:
            w[i]=0
        else:
            w[i]=1
    r=(w[7]+w[6]*2+w[5]*2**2 + w[4]*2**3 + w[3]*2**4 +w[2]*2**5 + w[1]*2**6 + w[0]*2**7)
    return r
    
    
  
    

try:
    a=0
    start=time.time()
    while a<=249:
        a=adc()
        end=time.time()
        time1.append(round((end-start),2)) 
        print("Напряжение на конденсаторе",a) #Находим напряжение на конденсаторе при зарядке
        f.append(str(a))

    GPIO.setup(troyka,GPIO.OUT,initial=0) 

    while a>=3:
        a=adc()
        end=time.time()
        time1.append(round((end-start),2))
        print("Напряжение на конденсаторе",a) #Находим напряжение на конденсаторе при разрядке
        f.append(str(a))
    end1=time.time()
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()

#Данные опыта
print("Общая продолжительность эксперимента",(end1-start))
print("Период измерения",(end1-start)/len(f))
print("Частота дискретизации",len(f)/(end1-start))
print("Шаг квантования",3.3/255)


#Сохранение полученных экспериментально данных в файлы
f1=[str(i) for i in f]
time2=[str(i) for i in time1]

#Файл со значениями напряжения на конденсаторе
with open('data.txt','w') as outfile:
    outfile.write("\n".join(f1))

#Файл со значение времени выполнения каждого эксперимента
with open('time.txt','w') as outfile:
    outfile.write("\n".join(time2))

#Файл со значением частоты и шага дискретизации
with open('settings.txt','w') as outfile:
    outfile.write("Частота дискретизации","\n")
    outfile.write(str((end1-start)/len(f)),"\n")
    outfile.write("Шаг дискретизации","\n")
    outfile.write(str(3.3/255))
plt.plot(f1)
plt.show()


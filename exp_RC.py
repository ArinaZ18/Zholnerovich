import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8,5),dpi=150)
settings = np.loadtxt("settings_1.txt", dtype=float)
data_array = np.loadtxt("data_1.txt", dtype=float)

data_array=data_array*settings[1]
time=np.arange(len(data_array))
time=time*0.0134
total_time=len(data_array)*settings[0]

plt.xlabel("Время,с",fontsize=12)
plt.ylabel("Напряжение,В",fontsize=12)
plt.title("Процесс заряда и разряда конденсатора в RC-цепи", fontsize=12,loc='center',fontweight='bold',style='italic')



time_ful=round(np.argmax(data_array)*settings[0],2)
time_empty=round(total_time-time_ful,2)

s_1="Время зарядки =" + str(time_ful) +" c"
s_2="Время разрядки =" + str(time_empty) +" c"
plt.text(64.5,2.9,s_1, fontsize=10)
plt.text(64.5,2.6,s_2, fontsize=10)

plt.grid(which='major',color='#A0A0A0')
plt.minorticks_on()
plt.grid(which='minor',color='#E0E0E0',linestyle='--')
plt.legend(loc="best")

plt.plot(time,data_array,linestyle='-',color='green',linewidth=0.25,label="U(t)")
plt.plot(time[::60],data_array[::60],linestyle=' ',marker='.',ms=3,color='blue')


plt.show()
fig.savefig("График U(t)")


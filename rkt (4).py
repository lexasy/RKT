from const0 import *       #объявили константы в "заголовочных" файлах
from const1 import *
from const2 import *
from const3 import *
from const4 import *
import math
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

def kk (M0, Mk, T0):   #формула рассчета расхода топлива за единицу времени
    return (M0 - Mk) // T0
G = 6.67 * (10 ** (-11))   #ускорение свободного падения
Mz = 5.97 * (10 ** 24)  #масса Земли
R = 6371 * (10 ** 3)    #радиус Земли




k0 = kk(W0_F, W0_E, T0) #вычисляем расход топлива
Ft0 = Thrust_0 #сила тяги определена в файлах с константами
H0 = []
V0 = []
TT0 = []
g0 = (G * Mz) / R ** 2   #ускорение свободного падения в определённый момент полёта
ay0 = (Ft0 / WR_0) * math.sin(math.radians(b0)) - g0   #ускорение по оси у, которая в будущем будет вычисляться ежесекундно
ax0 = (Ft0 / WR_0) * math.cos(math.radians(b0))      #ускорение по оси х, которая в будущем будет вычисляться ежесекундно
vy0 = v0 * math.sin(math.radians(b0)) + ay0     #скорость по оси у, которая в будущем будет вычисляться ежесекундно
vx0 = v0 * math.cos(math.radians(b0)) + ax0     #скорость по оси х, которая в будущем будет вычисляться ежесекундно

for t in range(T0):    #цикл для ежесекундного вычисления формул
    Mt = WR_0 - k0 * t    #масса топлива
    if t == 0:     
        h = h0
    else:
        h = h0 + vy0 + ay0 / 2 #высота
    H0.append(h / 10 ** 3) #переводим из СИ в км
    if t == 0:
        v = v0
    else:
        vy0 = v0 * math.sin(math.radians(b0)) + ay0
        vx0 = v0 * math.cos(math.radians(b0)) + ax0
        v = math.sqrt(vx0 ** 2 + vy0 ** 2)     #скорость
    ay0 = (Ft0 / Mt) * math.sin(math.radians(b0)) - g0
    ax0 = (Ft0 / Mt) * math.cos(math.radians(b0))
    g0 = (G * Mz) / (R + h) ** 2
    V0.append(v / 10 ** 3 * 3600) #переводим из СИ в км/ч
    b0 = b0 - u0 / T0
    h0 = h
    v0 = v

for t in range(t0, t0 + T0):
    TT0.append(t)

#реализация изображения мат моделей

figure0 = plt.figure()
figure0.suptitle('0 stage', fontsize=18)
ax1_0 = figure0.add_subplot(1, 2, 1)
ax2_0 = figure0.add_subplot(1, 2, 2)
ax1_0.plot(TT0, V0, color='red', label='v(s)')
ax2_0.plot(TT0, H0, color='green', label='h(s)')
ax1_0.legend(loc='lower right')
ax2_0.legend(loc='lower right')
ax1_0.set_xlabel("Time (s)")
ax1_0.set_ylabel("Speed (km/h)")
ax2_0.set_xlabel("Time (s)")
ax2_0.set_ylabel("Height (km)")

#точно такой же алгоритм применяем для оставшихся 4х ступеней

k1 = kk(W1_F, W1_E, T1)
Ft1 = Thrust_1 
H1 = []
V1 = []
TT1 = []
A1 = []
g1 = (G * Mz) / (R + h1) ** 2
ay1 = (Ft1 / WR_1) * math.sin(math.radians(b1)) - g1
ax1 = (Ft1 / WR_1) * math.cos(math.radians(b1))
vy1 = v1 * math.sin(math.radians(b1)) + ay1
vx1 = v1 * math.cos(math.radians(b1)) + ax1

for t in range(T1):
    Mt = WR_1 - k1 * t
    if t == 0:
        h = h1
    else:
        h = h1 + vy1 + ay1 / 2
    H1.append(h / 10 ** 3)
    if t == 0:
        v = v1
    else:
        vy1 = v1 * math.sin(math.radians(b1)) + ay1
        vx1 = v1 * math.cos(math.radians(b1)) + ax1
        v = math.sqrt(vx1 ** 2 + vy1 ** 2)
    ay1 = (Ft1 / Mt) * math.sin(math.radians(b1)) - g1
    ax1 = (Ft1 / Mt) * math.cos(math.radians(b1))
    g1 = (G * Mz) / (R + h) ** 2
    V1.append(v / 10 ** 3 * 3600)
    b1 = b1 - u1 / T1
    h1 = h
    v1 = v

for t in range(t1, t1 + T1):
    TT1.append(t)

figure1 = plt.figure()
figure1.suptitle('Ist stage', fontsize=18)
ax1_1 = figure1.add_subplot(1, 2, 1)
ax2_1 = figure1.add_subplot(1, 2, 2)
ax1_1.plot(TT1, V1, color='red', label='v(s)')
ax2_1.plot(TT1, H1, color='green', label='h(s)')
ax1_1.legend(loc='lower right')
ax2_1.legend(loc='lower right')
ax1_1.set_xlabel("Time (s)")
ax1_1.set_ylabel("Speed (km/h)")
ax2_1.set_xlabel("Time (s)")
ax2_1.set_ylabel("Height (km)")




k2 = kk(W2_F, W2_E, T2)
Ft2 = Thrust_2 
H2 = []
V2 = []
TT2 = []
A2 = []
g2 = (G * Mz) / (R + h2) ** 2
ay2 = (Ft2 / WR_2) * math.sin(math.radians(b2)) - g2
ax2 = (Ft2 / WR_2) * math.cos(math.radians(b2))
vy2 = v2 * math.sin(math.radians(b2)) + ay2
vx2 = v2 * math.cos(math.radians(b2)) + ax2

for t in range(T2):
    Mt = WR_2 - k2 * t
    if t == 0:
        h = h2
    else:
        h = h2 + vy2 + ay2 / 2
    H2.append(h / 10 ** 3)
    if t == 0:
        v = v2
    else:
        vy2 = v2 * math.sin(math.radians(b2)) + ay2
        vx2 = v2 * math.cos(math.radians(b2)) + ax2
        v = math.sqrt(vx2 ** 2 + vy2 ** 2)
    ay2 = (Ft2 / Mt) * math.sin(math.radians(b2)) - g2
    ax2 = (Ft2 / Mt) * math.cos(math.radians(b2))
    g2 = (G * Mz) / (R + h) ** 2
    V2.append(v / 10 ** 3 * 3600)
    b2 = b2 - u2 / T2
    h2 = h
    v2 = v




for t in range(t2, t2 + T2):
    TT2.append(t)

figure2 = plt.figure()
figure2.suptitle('IInd stage', fontsize=18)
ax1_2 = figure2.add_subplot(1, 2, 1)
ax2_2 = figure2.add_subplot(1, 2, 2)
ax1_2.plot(TT2, V2, color='red', label='v(s)')
ax2_2.plot(TT2, H2, color='green', label='h(s)')
ax1_2.legend(loc='lower right')
ax2_2.legend(loc='lower right')
ax1_2.set_xlabel("Time (s)")
ax1_2.set_ylabel("Speed (km/h)")
ax2_2.set_xlabel("Time (s)")
ax2_2.set_ylabel("Height (km)")





k3 = kk(W3_F, W3_E, T3)
Ft3 = Thrust_3 
H3 = []
V3 = []
TT3 = []
A3 = []
g3 = (G * Mz) / (R + h3) ** 2
ay3 = (Ft3 / WR_3) * math.sin(math.radians(b3)) - g3
ax3 = (Ft3 / WR_3) * math.cos(math.radians(b3))
vy3 = v3 * math.sin(math.radians(b3)) + ay3
vx3 = v3 * math.cos(math.radians(b3)) + ax3

for t in range(T3):
    Mt = WR_3 - k3 * t
    if t == 0:
        h = h3
    else:
        h = h3 + vy3 + ay3 / 2
    H3.append(h / 10 ** 3)
    if t == 0:
        v = v3
    else:
        vy3 = v3 * math.sin(math.radians(b3)) + ay3
        vx3 = v3 * math.cos(math.radians(b3)) + ax3
        v = math.sqrt(vx3 ** 2 + vy3 ** 2)
    ay3 = (Ft3 / WR_3) * math.sin(math.radians(b3)) - g3
    ax3 = (Ft3 / WR_3) * math.cos(math.radians(b3))
    g3 = (G * Mz) / (R + h) ** 2
    V3.append(v / 10 ** 3 * 3600)
    b3 = b3 - u3 / T3
    h3 = h
    v3 = v



for t in range(t3, t3 + T3):
    TT3.append(t)

figure3 = plt.figure()
figure3.suptitle('IIIrd stage', fontsize=18)
ax1_3 = figure3.add_subplot(1, 2, 1)
ax2_3 = figure3.add_subplot(1, 2, 2)
ax1_3.plot(TT3, V3, color='red', label='v(s)')
ax2_3.plot(TT3, H3, color='green', label='h(s)')
ax1_3.legend(loc='lower right')
ax2_3.legend(loc='lower right')
ax1_3.set_xlabel("Time (s)")
ax1_3.set_ylabel("Speed (km/h)")
ax2_3.set_xlabel("Time (s)")
ax2_3.set_ylabel("Height (km)")



k4 = kk(W4_F, W4_E, T4)
Ft4 = Thrust_4 
H4 = []
V4 = []
TT4 = []
A4 = []
g4 = (G * Mz) / (R + h4) ** 2
ay4 = (Ft4 / WR_4) * math.sin(math.radians(b4)) - g4
ax4 = (Ft4 / WR_4) * math.cos(math.radians(b4))
vy4 = v4 * math.sin(math.radians(b4)) + ay4
vx4 = v4 * math.cos(math.radians(b4)) + ax4

for t in range(T4):
    Mt = WR_4 - k4 * t
    if t == 0:
        h = h4
    else:
        h = h4 + vy4 + ay4 / 2
    H4.append(h / 10 ** 3)
    if t == 0:
        v = v4
    else:
        vy4 = v4 * math.sin(math.radians(b4)) + ay4
        vx4 = v4 * math.cos(math.radians(b4)) + ax4
        v = math.sqrt(vx4 ** 2 + vy4 ** 2)
    ay4 = (Ft4 / WR_4) * math.sin(math.radians(b4)) - g4
    ax4 = (Ft4 / WR_4) * math.cos(math.radians(b4))
    g4 = (G * Mz) / (R + h) ** 2
    V4.append(v / 10 ** 3 * 3600)
    b4 = b4 - u4 / T4
    h4 = h
    v4 = v




for t in range(t4, t4 + T4):
    TT4.append(t)

figure4 = plt.figure()
figure4.suptitle('IVth stage', fontsize=18)
ax1_4 = figure4.add_subplot(1, 2, 1)
ax2_4 = figure4.add_subplot(1, 2, 2)
ax1_4.plot(TT4, V4, color='red', label='v(s)')
ax2_4.plot(TT4, H4, color='green', label='h(s)')
ax1_4.legend(loc='lower right')
ax2_4.legend(loc='lower right')
ax1_4.set_xlabel("Time (s)")
ax1_4.set_ylabel("Speed (km/h)")
ax2_4.set_xlabel("Time (s)")
ax2_4.set_ylabel("Height (km)")
plt.show()

import numpy as np
import random
import math
import matplotlib.pyplot as plt


def szum_o_rozkladzie_jednostajnym(amplituda,t1,dlugosc,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    for x in range(len(fff)):
        fff[x]=random.uniform(-amplituda,amplituda)


def szum_gaussowski(t1,dlugosc,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    for x in range(len(fff)):
        fff[x]=random.gauss(0,1)




def sygnal_sinusoidalny(amplituda,okres,t1,dlugosc,czestotliwosc = 1000.0):
    fff = np.empty(int(dlugosc*czestotliwosc))
    for x in range(len(fff)):
        fff[x]=amplituda*math.sin((2*math.pi/okres)*(x/czestotliwosc))



def Sygnal_sinusoidalny_wyprostowany_jednopolowkowo(amplituda,okres,t1,dlugosc,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    for x in range(len(fff)):
        fff[x] = (1/2)*amplituda*( (math.sin((2 * math.pi / okres) * (x / czestotliwosc)))+abs(math.sin((2 * math.pi / okres) * (x / czestotliwosc))))



def Sygnal_sinusoidalny_wyprostowany_dwupolowkowo(amplituda,okres,t1,dlugosc,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    for x in range(len(fff)):
        fff[x] = abs(amplituda*math.sin((2*math.pi/okres)*(x/czestotliwosc)))



def Sygnal_prostokatny(amplituda,okres,t1,dlugosc,wypelnienie=0.5,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    lengthof1 = wypelnienie*okres*czestotliwosc
    xy = True
    for x in range(len(fff)):
        if x in np.arange(lengthof1,100000,okres*czestotliwosc):
           xy = False
        if (x in np.arange(okres*czestotliwosc,100000,okres*czestotliwosc)):
           xy = True
        if xy:
            fff[x]=amplituda
    fff[0]=0.0
    print(fff)
    plt.plot(fff)
    plt.show()

def Sygnal_prostokatny_symetryczny(amplituda,okres,t1,dlugosc,wypelnienie=0.5,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    lengthof1 = wypelnienie*okres*czestotliwosc
    xy = True

    for x in range(len(fff)):
        if x in np.arange(lengthof1,100000,okres*czestotliwosc):
           xy = False
        if (x in np.arange(okres*czestotliwosc,100000,okres*czestotliwosc)):
           xy = True
        if xy:
            fff[x]=amplituda
        else:
            fff[x]=-amplituda
    fff[0]=-amplituda
    print(fff)
    plt.plot(fff)
    plt.show()

def trojkatny(amplituda,okres,t1,dlugosc,wypelnienie=0.5,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc * czestotliwosc))
    lengthofincrease = wypelnienie * okres * czestotliwosc
    xy = True
    y=0

    for x in range(len(fff)):
        if x in np.arange(lengthofincrease, 100000, okres * czestotliwosc):
            xy = False
        if (x in np.arange(okres * czestotliwosc, 100000, okres * czestotliwosc)):
            xy = True
            y-=okres*czestotliwosc
        if xy:
            fff[x] = amplituda/(wypelnienie*okres)*y/czestotliwosc
        else:
            fff[x] = -amplituda / (okres * (1 - wypelnienie)) * y / czestotliwosc + amplituda / (1 - wypelnienie)
        y+=1
    print(fff)
    plt.plot(fff)
    plt.show()
def skok_jednostkowy(amplituda,t1,dlugosc,ts,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    for x in range(len(fff)):
        if x/czestotliwosc < ts:
            fff[x]=0.0
        elif x/czestotliwosc==ts:
            fff[x]=1.0/2.0 * amplituda
        else:
            fff[x] = amplituda
    print(fff)
    plt.plot(fff)
    plt.show()

def impuls_jednostkowy(amplituda,ns,n1,dlugosc,czestotliwosc=10.0):
    fff = np.empty(int(dlugosc * czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        if x == ns:
            fff[x]=amplituda
        else:
            fff[x]=0.0
        time_stamp[x]=x/czestotliwosc
    plt.scatter(time_stamp,fff)
    plt.show()

def szum_impulsowy(amplituda,t1,dlugosc,prawdopodobienstwo,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    prawdopodobienstwo=int(prawdopodobienstwo*1000)
    for x in range(len(fff)):
        if random.randrange(1000)<=prawdopodobienstwo:
            fff[x]=amplituda
        else:
            fff[x]=0.0
        time_stamp[x]=x/czestotliwosc
    plt.scatter(time_stamp, fff)
    plt.show()
# szum_o_rozkladzie_jednostajnym(1,0.0,0.1)
# szum_gaussowski(0.0,0.1)
# sygnal_sinusoidalny(1.0,1,0,2)
# Sygnal_sinusoidalny_wyprostowany_jednopolowkowo(1.0,1,0,2)
# Sygnal_sinusoidalny_wyprostowany_dwupolowkowo(1.0,1,0,2)
# Sygnal_prostokatny(1.0,1,0.0,8)
# Sygnal_prostokatny_symetryczny(1.0,1,0.0,8)
# trojkatny(1.0,1,0.0,8,0.2)
# skok_jednostkowy(1.0,0.0,4,2.0)
# impuls_jednostkowy(1.0,12,0,2,10)
szum_impulsowy(1.0,0.0,3,0.8,20.0)
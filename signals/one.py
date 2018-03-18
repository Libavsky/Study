import numpy as np
import random
import math
import matplotlib.pyplot as plt


def szum_o_rozkladzie_jednostajnym(amplituda,t1,dlugosc,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        fff[x]=random.uniform(-amplituda,amplituda)
        time_stamp[x] = x / czestotliwosc
    return fff,time_stamp


def szum_gaussowski(t1,dlugosc,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        fff[x]=random.gauss(0,1)
        time_stamp[x] = x / czestotliwosc
    return fff, time_stamp



def sygnal_sinusoidalny(amplituda,okres,t1,dlugosc,czestotliwosc = 1000.0):
    fff = np.empty(int(dlugosc*czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        fff[x]=amplituda*math.sin((2*math.pi/okres)*(x/czestotliwosc))
        time_stamp[x] = x / czestotliwosc
    return fff, time_stamp


def Sygnal_sinusoidalny_wyprostowany_jednopolowkowo(amplituda,okres,t1,dlugosc,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        fff[x] = (1/2)*amplituda*( (math.sin((2 * math.pi / okres) * (x / czestotliwosc)))+abs(math.sin((2 * math.pi / okres) * (x / czestotliwosc))))
        time_stamp[x] = x / czestotliwosc
    return fff, time_stamp

def Sygnal_sinusoidalny_wyprostowany_dwupolowkowo(amplituda,okres,t1,dlugosc,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        fff[x] = abs(amplituda*math.sin((2*math.pi/okres)*(x/czestotliwosc)))
        time_stamp[x] = x / czestotliwosc
    return fff, time_stamp

def Sygnal_prostokatny(amplituda,okres,t1,dlugosc,wypelnienie=0.5,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    lengthof1 = wypelnienie*okres*czestotliwosc
    xy = True
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        if x in np.arange(lengthof1,100000,okres*czestotliwosc):
           xy = False
        if (x in np.arange(okres*czestotliwosc,100000,okres*czestotliwosc)):
           xy = True
        if xy:
            fff[x]=amplituda
        time_stamp[x] = x / czestotliwosc
    fff[0]=0.0
    return fff, time_stamp
def Sygnal_prostokatny_symetryczny(amplituda,okres,t1,dlugosc,wypelnienie=0.5,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    lengthof1 = wypelnienie*okres*czestotliwosc
    xy = True
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        if x in np.arange(lengthof1,100000,okres*czestotliwosc):
           xy = False
        if (x in np.arange(okres*czestotliwosc,100000,okres*czestotliwosc)):
           xy = True
        if xy:
            fff[x]=amplituda
        else:
            fff[x]=-amplituda
        time_stamp[x] = x / czestotliwosc
    fff[0]=-amplituda
    return fff, time_stamp
def trojkatny(amplituda,okres,t1,dlugosc,wypelnienie=0.5,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc * czestotliwosc))
    lengthofincrease = wypelnienie * okres * czestotliwosc
    xy = True
    y=0
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
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
        time_stamp[x] = x / czestotliwosc
    return fff, time_stamp
def skok_jednostkowy(amplituda,t1,dlugosc,ts,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        if x/czestotliwosc < ts:
            fff[x]=0.0
        elif x/czestotliwosc==ts:
            fff[x]=1.0/2.0 * amplituda
        else:
            fff[x] = amplituda
        time_stamp[x] = x / czestotliwosc
    return fff, time_stamp

def impuls_jednostkowy(amplituda,ns,n1,dlugosc,czestotliwosc=10.0):
    fff = np.empty(int(dlugosc * czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        if x == ns:
            fff[x]=amplituda
        else:
            fff[x]=0.0
        time_stamp[x]=x/czestotliwosc
    return fff, time_stamp
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
    return fff, time_stamp

def amplituda_od_czasu_ciagly(dane,czas):
    plt.plot(czas,dane)
    plt.show()

def amplituda_od_czasu_dyskretny(dane, czas):
    plt.scatter(czas, dane)
    plt.show()

def histogram(dane,liczba_przedzialow):
    plt.hist(dane,liczba_przedzialow)
    plt.show()


def srednia(dane):
    return np.mean(dane)
def srednia_mod(dane):
    suma=0.0
    for x in dane:
        suma+=abs(x)
    return suma/len(dane)
def wariancja(dane):
    return np.var(dane)
def moc_srednia(dane):
    suma = 0.0
    for x in dane:
        suma+=x*x
    return suma/len(dane)
def wartosc_skuteczna(dane):
    suma = 0.0
    for x in dane:
        suma += x * x
    return math.sqrt(suma / len(dane))
def zapisz_sygnal(nazwa,dane,czas):
    temp = np.vstack((dane,czas))
    np.savetxt(nazwa,temp,delimiter=",")

def odczytaj_sygnal(nazwa):
    return np.loadtxt(nazwa,delimiter=",")
def dodaj(dane1,czas1,dane2,czas2):
    timeline = []
    if czas1[0]<czas2[0]:
        if czas1[len(czas1)-1]>czas2[len(czas2)-1]:
            for xx in czas1:
                timeline.append(xx)
        else:
            
    else:
        for xx in czas2:
            timeline.append(xx)


def odejmij(dane1,czas1,dane2,czas2):


def pomnoz(dane1,czas1,dane2,czas2):


def podziel(dane1,czas1,dane2,czas2):


x = szum_o_rozkladzie_jednostajnym(1,0.0,0.1)

y = szum_gaussowski(0.0,1.0)
amplituda_od_czasu_ciagly(y[0],y[1])
histogram(y[0],10)

zapisz_sygnal("foo.csv",y[0],y[1])
temp = odczytaj_sygnal("foo.csv")
#print(temp)
amplituda_od_czasu_ciagly(temp[0],temp[1])
histogram(temp[0],10)
# sygnal_sinusoidalny(1.0,1,0,2)
# Sygnal_sinusoidalny_wyprostowany_jednopolowkowo(1.0,1,0,2)
# Sygnal_sinusoidalny_wyprostowany_dwupolowkowo(1.0,1,0,2)
# Sygnal_prostokatny(1.0,1,0.0,8)
# Sygnal_prostokatny_symetryczny(1.0,1,0.0,8)
# trojkatny(1.0,1,0.0,8,0.2)
# skok_jednostkowy(1.0,0.0,4,2.0)
# impuls_jednostkowy(1.0,12,0,2,10)
# szum_impulsowy(1.0,0.0,3,0.8,20.0)
import math
import json
import matplotlib.pyplot as plt
import numpy
def splot(sygnal1, sygnal2):
    rezultat = []
    for n in range(0,len(sygnal1)+len(sygnal2)-1):
        sum = 0
        k = 0
        while (n-k)>=0:
            if n-k>=len(sygnal2) or k >= len(sygnal1):
                k+=1
                continue
            try:
                sum+=sygnal1[k]*sygnal2[n-k]
            except IndexError:
                print(n,k)
                print("exccc")
                sum+=0
            k+=1
        rezultat.append(sum)
    return rezultat
def korelacja(sygnal1, sygnal2):
    sygnal2.reverse()
    rezultat = []
    for n in range(0, len(sygnal1) + len(sygnal2) - 1):
        sum = 0
        k = 0
        while (n - k) >= 0:
            if n - k >= len(sygnal2) or k >= len(sygnal1):
                k += 1
                continue
            try:
                sum += sygnal1[k] * sygnal2[n - k]
            except IndexError:
                print(n, k)
                print("exccc")
                sum += 0
            k += 1
        rezultat.append(sum)
    return rezultat
def zwrocFiltr(rzadFiltru, K, okno = 0, dolno_gorno_srodkowo = 0):
    filtr = []
    for n in range(0,rzadFiltru):
        if n == (rzadFiltru-1)/2:
            x = (2.0/K)
        else:
            x = (math.sin((2.0*math.pi*(n - (rzadFiltru-1)/2) / K))) / (math.pi*(n - (rzadFiltru-1.0)/2.0))
        if okno == 1:
            x = x * (0.53836-0.46164* math.cos(2.0*math.pi*n/rzadFiltru))
        elif okno == 2:
            x = x * (0.5 - 0.5 * math.cos(2.0 * math.pi * n / rzadFiltru))
        elif okno == 3:
            x = x * (0.42-0.5 * math.cos(2.0 * math.pi * n / rzadFiltru) + 0.08 * math.cos(4.0 * math.pi * n / rzadFiltru))

        if dolno_gorno_srodkowo == 2:
            x = x*(2.0*math.sin(math.pi*n/2.0))
        elif dolno_gorno_srodkowo == 1:
            if n%2 == 1:
                x = -x
        filtr.append(x)
    return filtr


def obliczOdleglosc(sygnalSkorelowany, fProbkowania):
    x = (len(sygnalSkorelowany)//2)+1
    print(x)
    maxi = -10000000
    indexmaxi = x
    for i in range(x, len(sygnalSkorelowany)):
        if sygnalSkorelowany[i]>maxi:
            maxi = sygnalSkorelowany[i]
            indexmaxi = i
            print(maxi)
    zonk = indexmaxi-x
    print(zonk)
    czas = zonk/fProbkowania
    print(czas)
    return (300000000.0*czas)/2.0


def odczytajSygnal(sciezka):
    data = json.load(open(sciezka+".json"))
    return data
def opoznij(sygnal, oIle):
    doddo = []
    result = []
    for i in range(0,oIle):
        doddo.append(sygnal[i])
    for i in range(oIle,len(sygnal)):
        result.append(sygnal[i])
    for i in range(0,oIle):
        result.append(doddo[i])
    return result
# signal = [5,6,7]
# signal2 = [1,2,3,4]
# print(splot(signal,signal2))
filtr = zwrocFiltr(25,8,0,0)
plt.plot(filtr)
plt.show()
filtr = zwrocFiltr(63,8,1,0)
plt.plot(filtr)
plt.show()
filtr = zwrocFiltr(255,8,2,0)
plt.plot(filtr)
plt.show()
filtr = zwrocFiltr(511,64,3,0)
plt.plot(filtr)
plt.show()
filtr = zwrocFiltr(63,8,0,1)
plt.plot(filtr)
plt.show()
filtr = zwrocFiltr(511,64,3,1)
plt.plot(filtr)
plt.show()
filtr = zwrocFiltr(63,8,1,2)
plt.plot(filtr)
plt.show()
filtr = zwrocFiltr(511,64,3,2)
plt.plot(filtr)
plt.show()
# sygnal = odczytajSygnal("dodane")
# plt.plot(sygnal[0])
# plt.show()
# sygnalProst = odczytajSygnal("sinusoo")
# sygnalProst2 = odczytajSygnal("trojkatoo")
#
# splotten = splot(sygnalProst[0],sygnalProst2[0])
# korelaten = korelacja(sygnalProst[0],sygnalProst2[0])
# plt.plot(splotten)
# plt.show()
#
# plt.plot(korelaten)
# plt.show()
# print(len(sygnalProst2[0]))
# dzzzzt = opoznij(sygnalProst2[0],120)
# print(len(dzzzzt))
# plt.plot(sygnalProst[0])
# plt.show()
# plt.plot(dzzzzt)
# plt.show()
# filtr = zwrocFiltr(sygnal[0],1023,16.2,0,2)
#print(len(sygnalProst[0]))
#sploto = splot(sygnalProst2[0],sygnalProst[0])
#korelacjo = korelacja(sygnalProst[0],dzzzzt)
#plt.plot(sploto)
#plt.show()
# plt.plot(korelacjo)
# plt.show()
# print(obliczOdleglosc(korelacjo,2000))
# przefiltrowany = splot(filtr,sygnal[0])
# plt.plot(sygnal[1],sygnal[0])
# plt.show()
#
# plt.plot(sygnalProst[1],sygnalProst[0])
# plt.show()

# plt.plot(przefiltrowany)
# plt.show()

# doh = numpy.fft.rfft(filtr)
# modu = []
# moduDB = []
# c = doh.real
# for d in c:
#     d = abs(d)
#     modu.append(d)
#     moduDB.append(10.0*math.log(d))
# plt.plot(filtr)
# plt.show()

# plt.plot(sygnalProst[1],sygnalProst[0])
# plt.show()
#
# plt.plot(sygnalProst2[1],sygnalProst2[0])
# plt.show()

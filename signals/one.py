import numpy as np
import random
import math
import matplotlib.pyplot as plt
import msvcrt


def szum_o_rozkladzie_jednostajnym(amplituda,t1,dlugosc,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        fff[x]=random.uniform(-amplituda,amplituda)
        time_stamp[x] = round(t1 + x / czestotliwosc,12)
    return fff,time_stamp


def szum_gaussowski(amplituda,t1,dlugosc,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        fff[x]=amplituda*random.gauss(0,1)
        time_stamp[x] =round(t1 + x / czestotliwosc,12)
    return fff, time_stamp



def sygnal_sinusoidalny(amplituda,okres,t1,dlugosc,czestotliwosc = 1000.0):
    fff = np.empty(int(dlugosc*czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        fff[x]=round(amplituda*math.sin((2*math.pi/okres)*(x/czestotliwosc)),30)
        time_stamp[x] = round(t1 + x / czestotliwosc,12)
    return fff, time_stamp


def Sygnal_sinusoidalny_wyprostowany_jednopolowkowo(amplituda,okres,t1,dlugosc,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        fff[x] = (1/2)*amplituda*( (math.sin((2 * math.pi / okres) * (x / czestotliwosc)))+abs(math.sin((2 * math.pi / okres) * (x / czestotliwosc))))
        time_stamp[x] = round(t1 + x / czestotliwosc,12)
    return fff, time_stamp

def Sygnal_sinusoidalny_wyprostowany_dwupolowkowo(amplituda,okres,t1,dlugosc,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        fff[x] = abs(amplituda*math.sin((2*math.pi/okres)*(x/czestotliwosc)))
        time_stamp[x] = round(t1 + x / czestotliwosc,12)
    return fff, time_stamp

def Sygnal_prostokatny(amplituda,okres,t1,dlugosc,wypelnienie=0.5,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    lengthof1 = wypelnienie*okres*czestotliwosc
    xy = True
    time_stamp = np.zeros(int(dlugosc * czestotliwosc),dtype=float)
    for x in range(len(fff)):
        if x in np.arange(lengthof1,100000,okres*czestotliwosc):
            xy = False
        if (x in np.arange(okres*czestotliwosc,100000,okres*czestotliwosc)):
            xy = True
        if xy:
            fff[x]=amplituda
        else:
            fff[x]=0.0
        time_stamp[x] = round(t1 + x / czestotliwosc,12)
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
        time_stamp[x] = round(t1 + x / czestotliwosc,12)
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
        time_stamp[x] = round(t1 + x / czestotliwosc,12)
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
        time_stamp[x] = round(t1 + x / czestotliwosc,12)
    return fff, time_stamp

def impuls_jednostkowy(amplituda,ns,n1,dlugosc,czestotliwosc=10.0):
    fff = np.empty(int(dlugosc * czestotliwosc))
    time_stamp = np.empty(int(dlugosc * czestotliwosc))
    for x in range(len(fff)):
        if x == ns:
            fff[x]=amplituda
        else:
            fff[x]=0.0
        time_stamp[x]= round(n1 + x / czestotliwosc,12)
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
        time_stamp[x]=round(t1 + x / czestotliwosc,12)
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
def dane_wykresy_ciagle(dane,czas,przedzialy):
    print("Wartosc srednia: ", srednia(dane))
    print("Wartosc srednia bezwzgledna: ", srednia_mod(dane))
    print("Moc srednia: ", moc_srednia(dane))
    print("Wariancja: ", wariancja(dane))
    print("Wartosc skuteczna: ", wartosc_skuteczna(dane))
    amplituda_od_czasu_ciagly(dane,czas)
    histogram(dane,przedzialy)
def dane_wykresy_dyskretne(dane,czas,przedzialy):
    print("Wartosc srednia: ", srednia(dane))
    print("Wartosc srednia bezwzgledna: ", srednia_mod(dane))
    print("Moc srednia: ", moc_srednia(dane))
    print("Wariancja: ", wariancja(dane))
    print("Wartosc skuteczna: ", wartosc_skuteczna(dane))
    amplituda_od_czasu_dyskretny(dane,czas)
    histogram(dane,przedzialy)

def zapisz_sygnal(nazwa,arr):
    #temp = np.vstack((dane,czas))
    np.save(nazwa,arr)
    #np.savetxt(nazwa+".csv",arr,delimiter=",")

def odczytaj_sygnal(nazwa):
    return np.load(nazwa+".npy")
    # return np.loadtxt(nazwa,delimiter=",")
def dodaj(dane1,czas1,dane2,czas2):
    timeline = []
    if czas1[0]<czas2[0]:
        timeline.append(czas1[0])
    else:
        timeline.append(czas2[0])
    endtime = 0
    if czas1[len(czas1)-1]<czas2[len(czas2)-1]:
        endtime=czas2[len(czas2)-1]
    else:
        endtime = czas1[len(czas1) - 1]
    okres =  (czas1[1]-czas1[0])
    time = timeline[0]
    while time<endtime:
        time=round(time+okres,12)
        timeline.append(time)
    dane1_licznik = 0
    dane2_licznik = 0
    time_licznik = 0
    wynik = np.zeros(len(timeline),dtype=float)
    while time_licznik<len(timeline):
        if dane1_licznik< len(dane1) and czas1[dane1_licznik] == timeline[time_licznik]:
            wynik[time_licznik]+=dane1[dane1_licznik]
            dane1_licznik+=1
        if dane2_licznik< len(dane2) and czas2[dane2_licznik] == timeline[time_licznik]:
            wynik[time_licznik]+=dane2[dane2_licznik]
            dane2_licznik+=1
        time_licznik+=1
    return wynik,timeline



def odejmij(dane1,czas1,dane2,czas2):
    timeline = []
    if czas1[0]<czas2[0]:
        timeline.append(czas1[0])
    else:
        timeline.append(czas2[0])
    endtime = 0
    if czas1[len(czas1)-1]<czas2[len(czas2)-1]:
        endtime=czas2[len(czas2)-1]
    else:
        endtime = czas1[len(czas1) - 1]
    okres =  (czas1[1]-czas1[0])
    time = timeline[0]
    while time<endtime:
        time=round(time+okres,12)
        timeline.append(time)
    dane1_licznik = 0
    dane2_licznik = 0
    time_licznik = 0
    wynik = np.zeros(len(timeline),dtype=float)
    while time_licznik<len(timeline):
        if dane1_licznik< len(dane1) and czas1[dane1_licznik] == timeline[time_licznik]:
            wynik[time_licznik]+=dane1[dane1_licznik]
            dane1_licznik+=1
        if dane2_licznik< len(dane2) and czas2[dane2_licznik] == timeline[time_licznik]:
            wynik[time_licznik]-=dane2[dane2_licznik]
            dane2_licznik+=1
        time_licznik+=1
    return wynik,timeline

def pomnoz(dane1,czas1,dane2,czas2):
    timeline = []
    if czas1[0]<czas2[0]:
        timeline.append(czas1[0])
    else:
        timeline.append(czas2[0])
    endtime = 0
    if czas1[len(czas1)-1]<czas2[len(czas2)-1]:
        endtime=czas2[len(czas2)-1]
    else:
        endtime = czas1[len(czas1) - 1]
    okres =  (czas1[1]-czas1[0])
    time = timeline[0]
    while time<endtime:
        time=round(time+okres,12)
        timeline.append(time)
    dane1_licznik = 0
    dane2_licznik = 0
    time_licznik = 0
    wynik = np.zeros(len(timeline),dtype=float)
    while time_licznik<len(timeline):
        if dane1_licznik< len(dane1) and dane2_licznik< len(dane2) and czas1[dane1_licznik] == timeline[time_licznik] and czas2[dane2_licznik] == timeline[time_licznik]:
            wynik[time_licznik]=dane1[dane1_licznik]*dane2[dane2_licznik]
            dane1_licznik+=1
            dane2_licznik+=1
        elif dane1_licznik< len(dane1) and dane2_licznik< len(dane2) and czas2[dane2_licznik] == timeline[time_licznik] and czas1[dane1_licznik] != timeline[time_licznik]:
            wynik[time_licznik]=0.0
            dane2_licznik+=1
        elif dane1_licznik< len(dane1) and dane2_licznik< len(dane2) and czas1[dane1_licznik] == timeline[time_licznik] and czas2[dane2_licznik] != timeline[time_licznik]:
            wynik[time_licznik]=0.0
            dane1_licznik+=1
        else:
            wynik[time_licznik]= 0.0
        time_licznik+=1
    return wynik,timeline

def podziel(dane1,czas1,dane2,czas2):
    timeline = []
    if czas1[0]<czas2[0]:
        timeline.append(czas1[0])
    else:
        timeline.append(czas2[0])
    endtime = 0
    if czas1[len(czas1)-1]<czas2[len(czas2)-1]:
        endtime=czas2[len(czas2)-1]
    else:
        endtime = czas1[len(czas1) - 1]
    okres =  (czas1[1]-czas1[0])
    time = timeline[0]
    while time<endtime:
        time=round(time+okres,12)
        timeline.append(time)
    dane1_licznik = 0
    dane2_licznik = 0
    time_licznik = 0
    wynik = np.zeros(len(timeline),dtype=float)
    while time_licznik<len(timeline):
        if dane1_licznik< len(dane1) and dane2_licznik< len(dane2) and czas1[dane1_licznik] == timeline[time_licznik] and czas2[dane2_licznik] == timeline[time_licznik]:
            if dane2[dane2_licznik]==0.0 and dane1[dane1_licznik]==0.0:
                if time_licznik==0:
                    wynik[time_licznik]=0.0
                else:
                    wynik[time_licznik]=wynik[time_licznik-1]
                dane1_licznik += 1
                dane2_licznik += 1
                time_licznik+=1
                continue
            elif dane2[dane2_licznik]==0.0:
                wynik[time_licznik]=0.0
                dane1_licznik += 1
                dane2_licznik += 1
                time_licznik += 1
                continue
            wynik[time_licznik]=dane1[dane1_licznik]/dane2[dane2_licznik]
            dane1_licznik+=1
            dane2_licznik+=1
        elif dane1_licznik< len(dane1) and dane2_licznik< len(dane2) and czas2[dane2_licznik] == timeline[time_licznik] and czas1[dane1_licznik] != timeline[time_licznik]:
            wynik[time_licznik]=0.0
            dane2_licznik+=1
        elif dane1_licznik< len(dane1) and dane2_licznik< len(dane2) and czas1[dane1_licznik] == timeline[time_licznik] and czas2[dane2_licznik] != timeline[time_licznik]:
            wynik[time_licznik]=0.0
            dane1_licznik+=1
        else:
            wynik[time_licznik]= 0.0
        time_licznik+=1
    return wynik,timeline

def menu():
    Signals = []
    counter = 1
    x = 1
    while x < 6:
        print("1 - generacja sygnalu\n"
              "2 - zapis sygnalu\n"
              "3 - odczyt sygnalu\n"
              "4 - operacje na sygnalach\n"
              "5 - dane o sygnalach + wykresy\n\n"
              "Dostepne sygnaly:")
        for xx in Signals:
            print(xx[1],xx[2],xx[3])
        x = int(input())
        msvcrt.getch()
        if x == 1:
            while msvcrt.kbhit():
                msvcrt.getch()
            y = generacja_sygnalu()
            Signals.append((y[0],y[1],y[2],counter))
            counter+=1
        if x == 2:
            print("Prosze podac numer sygnalu:")
            numer = int(input())
            msvcrt.getch()
            print("Prosze podac nazwe pliku do zapisu:")
            nazwa = input()
            while msvcrt.kbhit():
                msvcrt.getch()
            zapisz_sygnal(nazwa,Signals[numer-1])
        if x == 3:
            print("Prosze podac nazwe pliku do odczytu:")
            nazwa = input()
            while msvcrt.kbhit():
                msvcrt.getch()
            odczytany = odczytaj_sygnal(nazwa)
            Signals.append((odczytany[0],odczytany[1],odczytany[2],counter))
            counter += 1
        if x == 4:
            print("Uwaga - dokonywac mozna operacji jedynie na sygnalach o takiej samej czestotliwosci probkowania:")
            print("Prosze podac numer sygnalu pierwszego:")
            pierwszy = int(input())
            msvcrt.getch()
            print("Prosze podac numer sygnalu drugiego:")
            drugi = int(input())
            msvcrt.getch()
            print("1 - dodawanie\n"
                  "2 - odejmowanie\n"
                  "3 - mnozenie\n"
                  "4 - dzielenie\n")
            print("Prosze wybrac operacje:")
            operacja = int(input())
            msvcrt.getch()
            if operacja == 1:
                Signals.append((dodaj(Signals[pierwszy-1][0][0],Signals[pierwszy-1][0][1],Signals[drugi-1][0][0],Signals[drugi-1][0][1]),"Wynik dodawania",Signals[pierwszy-1][2],counter))
                counter+=1
            if operacja == 2:
                Signals.append((odejmij(Signals[pierwszy-1][0][0],Signals[pierwszy-1][0][1],Signals[drugi-1][0][0],Signals[drugi-1][0][1]),"Wynik odejmowania",Signals[pierwszy-1][2],counter))
                counter+=1
            if operacja == 3:
                Signals.append((pomnoz(Signals[pierwszy-1][0][0],Signals[pierwszy-1][0][1],Signals[drugi-1][0][0],Signals[drugi-1][0][1]),"Wynik mnozenia",Signals[pierwszy-1][2],counter))
                counter+=1
            if operacja == 4:
                Signals.append((podziel(Signals[pierwszy-1][0][0],Signals[pierwszy-1][0][1],Signals[drugi-1][0][0],Signals[drugi-1][0][1]),"Wynik dzielenia",Signals[pierwszy-1][2],counter))
                counter+=1
        if x == 5:
            print("Prosze podac numer sygnalu:")
            numer = int(input())
            msvcrt.getch()
            przedzialy_ = int(input("Prosze podac liczbe przedzialow histogramu:"))
            msvcrt.getch()
            if Signals[numer-1][1]=="Impuls jednostkowy" or Signals[numer-1][1]=="Szum impulsowy":
                dane_wykresy_dyskretne(Signals[numer-1][0][0],Signals[numer-1][0][1],przedzialy_)
            else:
                dane_wykresy_ciagle(Signals[numer-1][0][0], Signals[numer-1][0][1],przedzialy_)





def generacja_sygnalu():
    print("Prosze wybrac sygnal\n"
          "1 - Szum o rozkladzie jednostajnym\n"
          "2 - Szum gaussowski\n"
          "3 - Sygnal sinusoidalny\n"
          "4 - Sygnal sinusoidalny wyprostowany jednopolowkowo\n"
          "5 - Sygnal sinusoidalny wyprostowany dwupolowkowo\n"
          "6 - Sygnal prostokatny\n"
          "7 - Sygnal prostokatny symetryczny\n"
          "8 - Sygnal trojkatny\n"
          "9 - Skok jednostkowy\n"
          "10 - Impuls jednostkowy\n"
          "11 - Szum impulsowy")
    z = int(input())
    msvcrt.getch()
    zz = float(input("Prosze podac czestotliwosc probkowania do zapisu"))
    msvcrt.getch()
    return f(z,zz)

def f(ccc,freq):
    if ccc == 1 or ccc == 2:
        print("Prosze podac:\n"
              "Amplituda\n"
              "Moment poczatkowy\n"
              "Dlugosc sygnalu")
        amp = float(input())
        msvcrt.getch()
        t1 = float(input())
        msvcrt.getch()
        d = float(input())
        msvcrt.getch()
        if ccc == 1:
            return szum_o_rozkladzie_jednostajnym(amp,t1,d,freq),"Szum o rozkladzie jednostajnym",str(freq)+"HZ"
        else:
            return szum_gaussowski(amp,t1,d,freq),"Szum gaussowski",str(freq)+"HZ"
    if ccc == 3 or ccc == 4 or ccc == 5:
        print("Prosze podac:\n"
              "Amplituda\n"
              "Okres\n"
              "Moment poczatkowy\n"
              "Dlugosc sygnalu")
        amp = float(input())
        msvcrt.getch()
        t=float(input())
        msvcrt.getch()
        t1 = float(input())
        msvcrt.getch()
        d = float(input())
        msvcrt.getch()
        if ccc == 3:
            return sygnal_sinusoidalny(amp, t, t1,d,freq),"Sygnal sinusoidalny",str(freq)+"HZ"
        elif ccc == 4:
            return Sygnal_sinusoidalny_wyprostowany_jednopolowkowo(amp,t,t1,d,freq),"Sygnal sinusoidalny wyprostowany jednopolowkowo",str(freq)+"HZ"
        else:
            return Sygnal_sinusoidalny_wyprostowany_dwupolowkowo(amp,t, t1, d,freq),"Sygnal sinusoidalny wyprostowany dwupolowkowo",str(freq)+"HZ"
    if ccc == 6 or ccc == 7 or ccc == 8:
        print("Prosze podac:\n"
              "Amplituda\n"
              "Okres\n"
              "Moment poczatkowy\n"
              "Dlugosc sygnalu\n"
              "Wypelnienie")
        amp = float(input())
        msvcrt.getch()
        t=float(input())
        msvcrt.getch()
        t1 = float(input())
        msvcrt.getch()
        d = float(input())
        msvcrt.getch()
        k = float(input())
        msvcrt.getch()
        if ccc == 3:
            return Sygnal_prostokatny(amp, t, t1,d,k,freq),"Sygnal prostokatny",str(freq)+"HZ"
        elif ccc == 4:
            return Sygnal_prostokatny_symetryczny(amp,t,t1,d,k,freq),"Sygnal prostokatny symetryczny",str(freq)+"HZ"
        else:
            return trojkatny(amp,t, t1, d,k,freq),"Sygnal trojkatny",str(freq)+"HZ"
    if ccc == 9:
        print("Prosze podac:\n"
              "Amplituda\n"
              "Moment poczatkowy\n"
              "Dlugosc sygnalu\n"
              "Moment skoku")
        amp = float(input())
        msvcrt.getch()
        t1 = float(input())
        msvcrt.getch()
        d = float(input())
        msvcrt.getch()
        ts = float(input())
        msvcrt.getch()
        return szum_o_rozkladzie_jednostajnym(amp, t1, d,ts,freq),"Skok jednostkowy",str(freq)+"HZ"
    if ccc == 10:
        print("Prosze podac:\n"
              "Amplituda\n"
              "Numer probki z impulsem\n"
              "Numer pierwszej probki\n"
              "Dlugosc sygnalu")
        amp = float(input())
        msvcrt.getch()
        ns = int(input())
        msvcrt.getch()
        n1 = int(input())
        msvcrt.getch()
        d = float(input())
        msvcrt.getch()
        return impuls_jednostkowy(amp,ns,n1,d,freq),"Impuls jednostkowy",str(freq)+"HZ"
    if ccc == 11:
        print("Prosze podac:\n"
              "Amplituda\n"
              "Moment poczatkowy\n"
              "Dlugosc sygnalu\n"
              "Prawdopodobienstwo impulsu")
        amp = float(input())
        msvcrt.getch()
        t1 = float(input())
        msvcrt.getch()
        d = float(input())
        msvcrt.getch()
        ts = float(input())
        msvcrt.getch()
        return szum_impulsowy(amp, t1, d, ts,freq),"Szum impulsowy",str(freq)+"HZ"
    else:
        print("\n" * 100)
        print("Bledna wartosc\n")
        menu()
menu()
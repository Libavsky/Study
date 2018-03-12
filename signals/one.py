import numpy as np
import random
print("lol")

def szum_o_rozkladzie_jednostajnym(amplituda,t1,dlugosc,czestotliwosc = 1000.0):
    random.seed()
    fff = np.empty(int(dlugosc*czestotliwosc))
    for x in range(len(fff)):
        fff[x]=random.uniform(-amplituda,amplituda)
    print(fff)


szum_o_rozkladzie_jednostajnym(1,2.0,0.01)
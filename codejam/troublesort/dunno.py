def TroubleSort(L):
    done = False
    while not done:
      done = True
      for i in range(0,len(L)-2):
        if L[i] > L[i+2]:
          done = False
          x = L[i]
          L[i]=L[i+2]
          L[i+2]=x
def check(numbers):
    for z in range(0,len(numbers)-1):
        if numbers[z+1]<numbers[z]:
            return z
    return -1
T = int(input())
Output = []
x = 1
while T>0:
    input()
    numbers = [int(s) for s in input().split(" ")]
    TroubleSort(numbers)
    y = check(numbers)
    if y==-1:
        Output.append("Case #" + str(x) + ": OK")
    else:
        Output.append("Case #" + str(x) + ": "+str(y))
    x+=1
    T -= 1
for lol in Output:
    print(lol)
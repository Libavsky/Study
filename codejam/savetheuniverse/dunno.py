def check_dmg(actual_orders):
    dmg = 0
    currentPower=1
    for x in actual_orders:
        if x == 0:
            currentPower*=2
        else:
            dmg+=currentPower
    return dmg
def doAHack(actual_orders):
    currentOrder=2
    lastOrder=2
    position=len(actual_orders)-1
    while position>=0:
        lastOrder=currentOrder
        currentOrder=actual_orders[position]
        if currentOrder == 0 and lastOrder == 1:
            actual_orders[position]=1
            actual_orders[position+1]=0
            return
        position-=1
T = int(input())
Output = []
x = 1
while T>0:
    D, P = [s for s in input().split(" ")]
    numberOfHacks = 0
    numberOfShots = 0
    D = int(D)
    numberRepresentation = []
    Output.append("Case #"+str(x)+": ")
    for c in P:
        if c == "C":
            numberRepresentation.append(0)
        else:
            numberRepresentation.append(1)
            numberOfShots += 1
    if D >=  check_dmg(numberRepresentation):
        print(check_dmg(numberRepresentation))
        Output[x-1] += "0"
        x += 1
        T -= 1
        continue
    elif numberOfShots>D:
        Output[x - 1] += "IMPOSSIBLE"
        x += 1
        T -= 1
        continue
    else:
        while check_dmg(numberRepresentation) > D:
            doAHack(numberRepresentation)
            numberOfHacks += 1
    Output[x - 1] += str(numberOfHacks)
    x += 1
    T -= 1
for lol in Output:
    print(lol)
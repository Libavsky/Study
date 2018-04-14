def choNum(array, xPoint, yPoint):
    ret = 0
    for i in range(xPoint[1],yPoint[1]):
        for j in range(xPoint[0],yPoint[0]):
            if array[j][i] == "@":
                ret+=1
    return ret
T = int(input())
Output = []
x = 1
while T>0:
    possible = 0
    R, C, H, V= [int(s) for s in input().split(" ")]
    rows=[]
    choPerMan=0
    for i in range(0,R):
        rows.append(input())
    for i in rows:
        for j in i:
            if str(j) == "@":
                choPerMan+=1
    choPerMan/=(H+1)*(V+1)
    for i in range(1,C):
        for j in range(1,R):
            if choNum(rows,(0,0),(j,i)) != choPerMan:
                continue
            if choNum(rows,(j,0),(R,i)) != choPerMan:
                continue
            if choNum(rows,(0,i),(j,C)) != choPerMan:
                continue
            if choNum(rows,(j,i),(R,C)) != choPerMan:
                continue
            possible+=1
    if possible!=0:
        Output.append("Case #" + str(x) + ": POSSIBLE")
    else:
        Output.append("Case #" + str(x) + ": IMPOSSIBLE")
    x+=1
    T -= 1
for lol in Output:
    print(lol)
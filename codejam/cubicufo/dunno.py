nodes = [[-0.5,-0.5,-0.5],[0.5,-0.5,-0.5],[0.5,0.5,-0.5],[-0.5,0.5,0.5],[0.5,0.5,0.5],[0.5,-0.5,0.5],[-0.5,0.5,-0.5],[-0.5,-0.5,0.5]]
def rotateZ3D(theta,nodes):
    import math
    sinTheta = math.sin(theta)
    cosTheta = math.cos(theta)
    for i in range(0,8):
        node = nodes[i]
        x = node[0]
        y = node[1]
        node[0] = x * cosTheta - y * sinTheta
        node[1] = y * cosTheta + x * sinTheta

def calculateArea(nodes):
    maxx = -1
    maxz = -1
    minx = 1
    minz = 1
    for d in nodes:
        if d[0]>maxx:
            maxx = d[0]
        if d[0]<minx:
            minx=d[0]
        if d[2]>maxz:
            maxz=d[2]
        if d[2]<minz:
            minz=d[2]
    return (maxx-minx)*(maxz-minz)

def calculateFacers(nodes):
        plmimi = nodes[1]
        mimipl = nodes[7]
        plplpl = nodes[4]
        miplmi = nodes[6]
        return (((plplpl[0]+plmimi[0])/2 , (plplpl[1]+plmimi[1])/2 ,(plplpl[2]+plmimi[2])/2),((plplpl[0]+miplmi[0])/2 ,(plplpl[1]+miplmi[1])/2 ,(plplpl[2]+miplmi[2])/2),
                ((plplpl[0]+mimipl[0])/2 ,(plplpl[1]+mimipl[1])/2 ,(plplpl[2]+mimipl[2])/2))
import math
import copy
globvar = 0
def findAngle(area_given,left,right,nodes):
    answer = 0
    leftRotation = copy.deepcopy(nodes)
    rightRotation = copy.deepcopy(nodes)
    rotateZ3D((left * math.pi) / 180, leftRotation)
    rotateZ3D((right * math.pi) / 180, rightRotation)
    if abs(calculateArea(leftRotation) - calculateArea(rightRotation))<0.000000000000001:
        global globvar
        if globvar!=0:
            return 0
        globvar = 1000000000
        return (left)
    if calculateArea(leftRotation)>area_given or calculateArea(rightRotation)<area_given:
        return 0
    x = (right - left)/5
    answer += findAngle(area_given,left,left+x,nodes)
    answer += findAngle(area_given, left + x, left + 2*x, nodes)
    answer += findAngle(area_given, left + 2*x, left + 3*x, nodes)
    answer += findAngle(area_given, left + 3*x, left + 4*x, nodes)
    answer += findAngle(area_given, left + 4*x, left + 5*x, nodes)
    return answer
T = int(input())
Output = []
x = 1
while T>0:
    globvar=0
    NODES = copy.deepcopy(nodes)
    area = float(input())
    cc = findAngle(area,0,45,NODES)
    rotateZ3D((cc * math.pi) / 180,NODES)
    zzz = calculateFacers(NODES)
    Output.append("Case #" + str(x) + ":\n"+str(zzz[0][0])+" "+str(zzz[0][1])+" "+str(zzz[0][2])
                  +"\n"+str(zzz[1][0])+" "+str(zzz[1][1])+" "+str(zzz[1][2])
                  + "\n" + str(zzz[2][0]) + " " + str(zzz[2][1]) + " " + str(zzz[2][2]))
    x+=1
    T -= 1
for lol in Output:
    print(lol)

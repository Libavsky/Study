#Toto do tego pierwszego
#Ten judge jest jakiś dziwny, w ogóle nie da się importować w pythonie
#Wydaje się być działające

def euclidean0_1(vector1, vector2):
    '''calculate the euclidean distance, no numpy
    input: numpy.arrays or lists
    return: euclidean distance
    '''
    dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
    dist = sum(dist)**(.5)
    return dist
def bipartiteMatch(graph):
    matching = {}
    for u in graph:
        for v in graph[u]:
            if v not in matching:
                matching[v] = u
                break
    while 1:
        preds = {}
        unmatched = []
        pred = dict([(u, unmatched) for u in graph])
        for v in matching:
            del pred[matching[v]]
        layer = list(pred)
        while layer and not unmatched:
            newLayer = {}
            for u in layer:
                for v in graph[u]:
                    if v not in preds:
                        newLayer.setdefault(v, []).append(u)
            layer = []
            for v in newLayer:
                preds[v] = newLayer[v]
                if v in matching:
                    layer.append(matching[v])
                    pred[matching[v]] = v
                else:
                    unmatched.append(v)
        if not unmatched:
            unlayered = {}
            for u in graph:
                for v in graph[u]:
                    if v not in preds:
                        unlayered[v] = None
            return (matching, list(pred), list(unlayered))
        def recurse(v):
            if v in preds:
                L = preds[v]
                del preds[v]
                for u in L:
                    if u in pred:
                        pu = pred[u]
                        del pred[u]
                        if pu is unmatched or recurse(pu):
                            matching[v] = u
                            return 1
            return 0

        for v in unmatched: recurse(v)
numbers = [int(s) for s in input().split(" ")]
gophers = []
holes = []
for i in range(0,int(numbers[0])):
    zonk = [float(s) for s in input().split(" ")]
    gophers.append(zonk)
for i in range(0,int(numbers[1])):
    zonk = [float(s) for s in input().split(" ")]
    holes.append(zonk)
gopher_can_run_for = numbers[2]*numbers[3]
graph = {}
for i in range(0,len(gophers)):
    da_list = []
    for z in range(0,len(holes)):
        dist = euclidean0_1(gophers[i], holes[z])
        if dist < gopher_can_run_for:
            da_list.append(z)
    graph[i]=da_list
answer = numbers[0] - len(bipartiteMatch(graph)[0])
print(int(answer))

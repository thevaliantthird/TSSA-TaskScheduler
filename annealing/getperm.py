import numpy as np
import random
import math
import useri.interact

def GetCombination(t2t, tb):
    s = np.sum(np.array(tb))
    z = (np.sum(np.array(list(t2t.values()))))
    print(t2t)
    taken = {}
    zi = t2t.copy()
    print(s,z)
    while s > 0:
        t = round(z*random.random())
        cum = 0
        #print(t,s)
        for x in t2t.keys():
            cum+=t2t[x]
            if cum > t and zi[x] > 0:
                if x in taken.keys():
                    taken[x]+=1
                else:
                    taken[x] = 1
                zi[x]-=1
                s -= 1
                break
    print(taken)
    return taken

def GetDifferentCombination(t2t,taken):
    c = t2t.copy()
    takem = taken.copy()
    for x in taken.keys():
        c[x] = c[x]-taken[x]
    
    chosen = -1
    for t in taken.keys():
        if random.random() < 0.1:
            chosen = x
            break
    if chosen==-1:
        chosen = list(taken.keys())[0]
    z = list(c.keys())
    random.shuffle(z)
    for t in z:
        if t != chosen and c[t] >= takem[chosen]:
            takem[t] += takem[chosen]
            del takem[chosen]
            break 
    return takem

def GetPermutation(taken):
    L = []
    for key in taken.keys():
        L.append((key,taken[key]))
    random.shuffle(L)
    return L

def GetDifferentPermutation(take):
    z = take.copy()
    i = 0
    j = 0
    
    while i==j:
        i = math.floor(len(take)*random.random())
        j = math.floor(len(take)*random.random())
    t = z[i]
    z[i] = z[j]
    z[j] = t
    return z
    
def BoltzmannFunction(e):
    return math.exp(-e)





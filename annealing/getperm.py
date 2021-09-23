import numpy as np
import random
import useri.interact

def GetCombination(t2t, tb):
    s = np.sum(np.array(tb))
    z = (np.sum(np.array(list(t2t.values()))) + 6)
    taken = {}
    while s > 0:
        t = round(z*random.random())
        cum = 0
        for x in t2t.keys():
            if cum > t:
                if x in taken.keys():
                    taken[x]+=1
                else:
                    taken[x] = 1
                s -= 1
                break
            else
                cum+=t2t[x]
    return taken

def GetDifferentCombination(t2t,taken):
    c = t2t.copy()
    for x in taken.keys():
        c[x] = c[x]-taken[x]
    
    chosen = -1
    for t in taken.keys():
        if random.random() < 0.1:
            chosen = x
            break
    if chosen==-1:
        chosen = list(taken.keys())[0]
    z = random.shuffle(list(c.keys()))
    for t in z:
        if t != chosen and c[t] >= taken[t]:
            taken[t] += taken[chosen]
            del taken[chosen]
            break 
    return taken

def GetPermutation(taken):
    L = []
    for key in taken.keys():
        L.append((key,taken[key]))
    return random.shuffle(L)

def GetDifferentPermutation(take):
    return random.shuffle(take)




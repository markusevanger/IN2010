from collections import defaultdict

# FIL INPUT SER SLIK UT:
# A B 13
# B C 2 
...

def bygg_graf(fil):

    V = set()
    E = defaultdict(set)
    w = {}

    for linje in fil:
        l = linje.strip().split(" ")

        V.add(l[0])
        V.add(l[1])

        E[l[0]].add(l[1])
        E[l[1]].add(l[0])

        w[(l[1], l[0])] = l[2]
        w[(l[0], l[1])] = l[2]
        
    return V, E, w


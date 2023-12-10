
seps = set()
depth = {}
low = {}

def SepNode(G):
    s = Some node in V
    depth[s] = 0
    low[s] = 0
    children = 0

    for (s, u) in E:
        if u not in depth:
            SepRec(G, s, u, 1)
            children += 1 
    if children > 1: 
        seps.add(s)
    return seps

def SepRec(G, p, u, d):

    depth[u] = d
    low[u] = d

    for (u, v) in E:
        if v == p: 
            continue
        if v in depth:
            low[u] = min(low[u], depth[v])
            continue
        SepRec(G, u, v, d+1)
        low[u] = min(low[u], low[v])

        if depth[u] <= low[v]:
            seps.add(u)
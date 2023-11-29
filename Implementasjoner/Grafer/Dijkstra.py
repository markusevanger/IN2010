import heapqueue


def Dijkstra(G, s):

    dist = {}
    priorityqueue = heapqueue()
    for v in V:
        dist[v] = float("inf") # sett til infinity
        priorityqueue.insert(v, dist[v]) # legg til med prioritet evig. 

    dist[s] = 0
    priorityqueue.decreasePriority(s, 0)
    
    while priorityqueue is not empty:
        u = priorityqueue.removeMin()
        for (u, v) in E:
            c = dist[u] + w(u, v)
            if c < dist[v]:
                dist[v] = c
                priorityqueue.decreasePriority(v, c)
    return dist


def Djikstra(G, s) #pseudocode.

    pq = empty priorityqueue
    dist = empty hashmap/dict

    for v in V:
        dist[v] = infinity
        Insert(pq, v with infinity priority)
    
    dist[s] = 0
    DecreasePriority(pq, s, 0)

    while pq is not empty:
        u = RemoveMin(pq)
        for (u, v) in E: # for hver kant til u:
            c = dist[u] + w(u, v) # akkumulert vekt til v = c
            if c < dist[v]: 
                dist[v] = c
                DecreasePriority(pq, v, c)
    return dist
                

    


























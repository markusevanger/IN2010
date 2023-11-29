from collections import deque



def BFSVisit(G, s, visited):

    queue = deque([s])
    while queue is not empty:
        u = queue.popleft()
        for (u, v) in E:
            if v not in visited:
                visited.add(u)
                queue.append(u)

def BFSFull(G):
    visited = set()
    for v in V:
        if v not in visited:
            visited.add(v)
            DFSVisit(G, v, visited)
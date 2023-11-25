

def DFS(G):
    
    V, E = G

    visited = set()
    for v in V:
        if v not in visited:
            print(v)
            visited.add(v)
            DFS_rek(E, v, visited)

    # skal bare printe alle noder i en gitt graf, dybde først. 

def DFS_rek(E, u, visited):


    for edge in E[u]:
        if edge not in visited:
            print(u)
            visited.add(edge)
            DFS_rek(E, edge, visited)



V = {"A", "B", "C", "D", "E", "F"}
E = {
    "A" : ["B", "C", "D"],
    "B" : ["A", "C"],
    "C" : ["A", "B", "D", "F"],
    "D" : ["A", "C", "E"],
    "E" : ["D", "F"],
    "F" : ["C", "E", "G"],
    "G" : ["F"],
}

DFS((V, E))

def BFSFull(G):
    visited = set()
    for v in G:
        if v not in visited:
            BFSVisit(G, v, visited)

def BFSVisit(G, s, visited):
    visited.add(s)
    queue = [s]
    while len(queue) > 0:
        print(queue)
        u = queue.pop()
        for v in G[u]:
            if v not in visited:
                visited.add(v)
                queue.insert(0, v)

def main():
    graf = {
        "A": ["B", "C", "D"],
        "B": ["A", "C"],
        "C": ["A", "B", "D", "F"],
        "D": ["A", "C", "E"],
        "E": ["D", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }
    BFSFull(graf)

main()
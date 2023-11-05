from VisualizeGraph import create_graph_image

def DFS(G, s, visited):
    
    stack = [s]
    while len(stack) > 0:
        print(stack)
        u = stack.pop(0)
        if u not in visited:
            visited.add(u)
            for v in G[u]:
                stack.insert(0, v)

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

    s = list(graf.keys())[0]
    DFS(graf, s, set())
    create_graph_image(graf)
    



main()
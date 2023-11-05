from VisualizeGraph import create_graph_image

# Tar imot en graf og sjekker alle noder. Viktig om grafen består av flere komponenter. 
def DFSFull(G):
    visited = set()
    for v in G: # iterer gjennom alle noder i grafen.
        if v not in visited: 
            print(v) # printer for å visualisere path
            DFSVisit(G, v, visited) # besøk nodens kanter


# Tar imot node "u", rekursivt kaller på seg selv med nodens kanter
def DFSVisit(G, u, visited):
    visited.add(u) # legg til node i visited

    for edge in G[u]: # iterer gjennom kantene til noden
        if edge not in visited: # sjekk om at vi ikke har sjekket noden kanten fører til før. 
            print(edge)
            DFSVisit(G, edge, visited) # rekursivt fortsett



def main():
    graf = {
        "A": ["D", "C", "B"],
        "B": ["A", "C"],
        "C": ["B", "A", "D", "F"],
        "D": ["A", "E", "C"],
        "E": ["D", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }
    create_graph_image(graf)
    DFSFull(graf)



main()
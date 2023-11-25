from collections import defaultdict
from VisualizeGraph import create__wgraph_image

# G = (V, E), w[(W,E)] = vekt
def bygg_graf(lines):

    V = set()
    E = defaultdict(set)
    w = {}

    for line in lines:
        line = line.strip().split(" ")

        V.add(line[0])
        V.add(line[1])
        E[line[0]].add(line[1])
        E[line[1]].add(line[0])

        w[(line[0], line[1])] = int(line[2])
        w[(line[1], line[0])] = int(line[2])
     
    return V, E, w


def main():
    
    FIL = "graf.txt"
    lines = open(FIL).readlines()
    G = bygg_graf(lines)
    #print(G[1])
    create__wgraph_image(G)
    

main()
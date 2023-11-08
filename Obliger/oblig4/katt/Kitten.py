#import graphviz
from collections import deque, defaultdict

def lag_tre():
    
    

    katt = input() # første linje inneholder noden katten er på. 
    G = defaultdict(set)

    ferdig = False
    while not ferdig:

        subtree = input()

        if subtree != "-1":

            subtree = subtree.split(" ")
            subroot_value = subtree[0]

            G[subroot_value] = subtree[1:]
            
        else:
            ferdig = True

    # all_trees = liste av alle input trær. 
    # Nå må vi merge alle trærne. 


    root = finn_rot(G)
    return G, root, katt
    
        


def finn_rot(G):
    has_parent = []
    for tree in G:
        for chld in G[tree]:
            has_parent.append(chld)
    
    return [tree for tree in G if tree not in has_parent][0]


def finn_katt(G, rot, katt):
    #print(f"Finner katt fra {rot} til katt {katt}...")

    parents = shortest_path_from(G, rot)
    v = katt
    path = []
    
    while v: 
        path.append(v)
        v = parents[v]

    return path
    

def shortest_path_from(G, rot):
    parents = {rot : None}
    queue = deque([rot])

    while queue: 
        u = queue.popleft()
        for edge in G[u]:
            if edge not in parents:          
                parents[edge] = u
                queue.append(edge)
    return parents



def main():
    
    G, rot, katt = lag_tre()
    #tegn_dict_repr_graf(G, rot)
    rute = finn_katt(G, rot, katt)
    
    
    for node in rute:
        print(node, end=" ")
    #print(f"Fant katt. Den må ta ruten {rute}")


def tegn_dict_repr_graf(G, rot):
    
    dot = graphviz.Graph(format='png', engine='dot' )
    
    for node, neighbors in G.items():
        for neighbor in neighbors:
            dot.edge(str(node), str(neighbor))  # Add an edge to each neighbor
    
    dot.render('graph')

main()
from collections import deque, defaultdict



# Denne versjonen er noe mer ueffektiv da den gjør et BFS søk i hele


class Node:
    def __init__(self, val, children, parent):

        self.value = val
        self.parent = parent
        self.children = []
        
        for child_val in children:
            self.children.append(Node(child_val, [], self)) # oppretter løv node med ingen egne barn, men har self som forelder.


    def change_childs(self, children):
        self.children = children
    
    def add_parent(self, parent):
        self.parent = parent

    def __str__(self):
        return str(self.value)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, other):
        return self.value == other.value



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


    root = finn_rot(G)
    return G, root, katt
    
        


def finn_rot(G):
    has_parent = []
    for tree in G:
        for chld in G[tree]:
            has_parent.append(chld)
    
    return [tree for tree in G if tree not in has_parent][0]


def finn_katt(G, rot, katt):

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
    rute = finn_katt(G, rot, katt)
    
    for node in rute:
        print(node, end=" ")

    
main()
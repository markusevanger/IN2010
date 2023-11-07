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
    
    

    katt = int(input()) # første linje inneholder noden katten er på. 
    G = {}

    ferdig = False
    while not ferdig:

        subtree = input()

        if subtree != "-1":

            subtree = subtree.split(" ")
            subroot_value = int(subtree[0])
            subtree_children = make_list_to_ints(subtree[1:])

            G[subroot_value] = subtree
            
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
    print(f"Finner katt fra {rot} til katt {katt}.")


def main():
    
    G, rot, katt = lag_tre()
    rute = finn_katt(G, rot, katt)








def value_in_tree(root, value):
    if root.value == value:
        return True
    
    for child in root.children:
        if value_in_tree(child, value) is True:
            return True
    
    return False

def make_list_to_ints(ls):
    for i in range(len(ls)):
        ls[i] = int(ls[i])
    return ls
    
main()
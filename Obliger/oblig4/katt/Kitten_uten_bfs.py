
from collections import defaultdict

def lag_tre():
    
    

    katt = input()

    E = defaultdict(set)
    A = set()

    ferdig = False
    while not ferdig:

        subtree = input()

        if subtree != "-1":

            subtree = subtree.split(" ")
            A.add(subtree[0])
            E[subtree[0]] = subtree[1:]
            
        else:
            ferdig = True

    return A, E, katt
    

def finn_foreldre(A, E):    
    
    parents = {}

    # linke opp alle sine foreldre
    for parent in E:
        for child in E[parent]:
            parents[child] = parent

    # finne hvilken som er rot, aka hvilken som aldri fant sin forelder . 
    for node in A:
        if node not in parents:
            parents[node] = None

    return parents

def finn_katt(parents, katt):
    
    rute = []
    current_plass = katt
    while current_plass != None:
        rute.append(current_plass)
        current_plass = parents[current_plass]

    return rute



def main():
        
    A, E, katt = lag_tre()
    parents = finn_foreldre(A, E)
    rute = finn_katt(parents, katt)
    
    for r in rute:
        print(r, end=" ")

main()
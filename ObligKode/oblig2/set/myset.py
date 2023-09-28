from TreTester import LiveTest, FyllTilfeldig, FyllKonstant
from Visualize import visualize
import sys

class Set:

    class Node:
        def __init__(self, x):
            self.element = x
            self.right = None
            self.left = None
            # self.parent = None 

    def __init__(self):
        self.root = None
        self.size = 0
    
    
    # Rekursivt finner frem til tom node på riktig None type løvnode og setter til ny Node(x)
    def insert(self, node, x): # O(log(n))

        # Vi har nådd løvnoden vi skal sette inn i / treet er tomt. 
        if node == None:
            node = self.Node(x)
            self.size += 1
        elif node.element > x: 
            node.left = self.insert(node.left, x)
        elif node.element < x:
            node.right = self.insert(node.right, x)
        # else er x = node.element, og vi trenger ikke sette inn.
        return node


    def contains(self, node, x):
        if node == None:
            return False
        if node.element == x:
            return True
        if node.element < x:
            return self.contains(node.right, x)
        if node.element > x:
            return self.contains(node.left, x)
 
    # Hjelpemetode slik at vi teller ned størrelsen kun på første kall og ikke på hvert rekursive kall. 
    def remove(self, x): # Kjøretid: O(2log(n)) 

        # sjekke om v er i treet, 
        if self.contains(self.root, x): # + O(log(n))
            self.size -= 1
        return self.removeRek(self.root, x) # + O(log(n))

    def removeRek(self, v, x):
        
        
        if v == None:
            return None
        
        # x er mindre enn elementet vi er i, dermed må vi lete videre i venstre subtre.
        if x < v.element:
            v.left = self.removeRek(v.left, x)
            return v
        
        # x er større enn elementet vi er i, dermed lete videre i høyre subtre
        if x > v.element:
            v.right = self.removeRek(v.right, x)
            return v
        
        # Om venstre peker ikke eksisterer
        if v.left == None:
            return v.right # vet vi at vi må returnere v.right. Har ingeting å si at v.right er null/None
        
        # Om Høyre peker ikke eksisterer
        if v.right == None:
            return v.left # vet vi at vi må returnere v.left.
        
        #  >> Nå er v noden vi ønsker å slette, og vi har to designerte barn.  << 
        
        u = self.findMin(v.right) # finn det minste elemente i det høyre subtreet
        v.element = u.element # v sitt element er nå det minste elementet i v´s subtre
        v.right = self.removeRek(v.right, u.element) # u har ikke et venstre subtre, da det er det minste elementet.
        return v

    def findMin(self, node):
        if node == None: # skal kun oppstå om roten er 0
            return None
        if node.left == None:
            return node
        return self.findMin(node.left)
    
def main():
    set = Set()

    LiveTest(set)
    set.remove(set.root, 10)
    LiveTest(set)

def kjor():

    set = Set()
    output_liste = []

    for i in range(int(input())):
        linje = input().split(" ")
        S = linje[0]

        if S == "size":
            output_liste.append(set.size)
        else:
            x = int(linje[1])
            if S == "insert":
                set.root = set.insert(set.root, x)
            if S == "contains":
                output_liste.append(set.contains(set.root, x))
            if S == "remove":
                    set.root = set.remove(x)

    visualize(set)

    for s in output_liste:
        print(s)

# main()
kjor()

    
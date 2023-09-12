from Visualize import visualize
from TreTester import LiveTest, FyllTilfeldig, FyllKonstant

class BinaryTree:

    class Node:
        def __init__(self, key):
            self.element = key
            self.left = None
            self.right = None
        
        def __str__(self):
            return str(self.element)

    def __init__(self):
        self.root = None

    def insert(self, v, x):
        if v == None:
            v = self.Node(x)
        elif v.element > x:
            v.left = self.insert(v.left, x)
        elif v.element < x:
            v.right = self.insert(v.right, x)
        return v

    def Search(self, v, x):
        if v == None:
            return None
        if v.element == x:
            return v
        if x < v.element:
            return self.Search(v.left, x)
        if x > v.element:
            return self.Search(v.right, x)
        
    def findMin(self, v):
        
        # Sjekker om lista eller noden oppgitt er tom/ugyldig. Ikke nødvendig
        if v == None: 
            return None  
        # v.left er alltid mindre enn v, dermed rekusivt sjekker vi om v.left har v.left.left
        elif v.left != None: 
            return self.findMin(v.left)
        # Stopper rekursivt kall når v.left == None. 
        else: 
            return v
        
    def Remove(self, v, x):
        
        # Kommet frem til tomt tre. Ting vi prøver å slette ikke eksister.
        if v == None:
            return None
        
        # x er mindre enn elementet vi er i, dermed må vi lete videre i venstre subtre.
        if x < v.element:
            v.left = self.Remove(v.left, x)
            return v
        
        # x er større enn elementet vi er i, dermed lete videre i høyre subtre
        if x > v.element:
            v.right = self.Remove(v.right, x)
            return v
        
        # Om venstre peker ikke eksisterer
        if v.left == None:
            return v.right # vet vi at vi må returnere v.right. Har ingeting å si at v.right er null/None
        
        # Om Høyre peker ikke eksisterer
        if v.right == None:
            return v.left # vet vi at vi må returnere v.left.
        
        #  >> Nå er vi ved noen vi ønsker å slette, og vi har to designerte barn.  << 
        
        u = self.findMin(v.right) # finn det minste elemente i det høyre subtreet
        v.element = u.element # v sitt element er nå det minste elementet i v´s subtre
        v.right = self.Remove(v.right, u.element) # u har ikke et venstre subtre, da det er det minste elementet.  
        return v



def test():
    b = BinaryTree() # opprett tre
    
    # LiveTest(b) # La bruker fylle
    # FyllTilfeldig(b, 10) # fyll tilfeldig x ganger
    FyllKonstant(b) # Fyller treet med samme input hver gang

    svar = input("Skriv hvilket tall du ønsker å fjerne: ")
    b.Remove(b.root, int(svar))
    visualize(b)


    print("Minste tall:", b.findMin(b.root))
    
test()

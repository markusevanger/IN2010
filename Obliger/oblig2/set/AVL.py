class AVL:

    # Node klasse
    class Node:
        def __init__(self, key):
            self.element = key
            self.left = None
            self.right = None
            self.height = 0
        
        def __str__(self):
            return str(self.element)

    # AVL Tre Klasse
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, v, x):
        if v == None:
            v = self.Node(x) ########
            self.size +=1
        elif v.element > x:
            v.left = self.insert(v.left, x)
        elif v.element < x:
            v.right = self.insert(v.right, x)

        v.height = 1 + max(self.Height(v.left), self.Height(v.right))
        return self.Balance(v)

    def contains(self, node, x):
        if node == None:
            return False
        if node.element == x:
            return True
        if node.element < x:
            return self.contains(node.right, x)
        if node.element > x:
            return self.contains(node.left, x)
        
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
        

    # Samme metode som i Set, for å korrigere høyden. 
    def remove(self, v, x): 
        if self.contains(self.root, x):
            self.size -= 1
        return self.removeRek(self.root, x)
        
    def removeRek(self, v, x):
        
        # Kommet frem til tomt tre. Ting vi prøver å slette ikke eksister.
        if v == None:
            return None
        
        # x er mindre enn elementet vi er i, dermed må vi lete videre i venstre subtre.
        if x < v.element:
            v.left = self.removeRek(v.left, x)
            return v
        
        # x er større enn elementet vi er i, dermed lete videre i høyre subtre
        elif x > v.element:
            v.right = self.removeRek(v.right, x)
            return v
        
        # Om venstre peker ikke eksisterer
        elif v.left == None:
            return v.right # vet vi at vi må returnere v.right. Har ingeting å si at v.right er null/None
        
        # Om Høyre peker ikke eksisterer
        elif v.right == None:
            return v.left # vet vi at vi må returnere v.left.
        
        #  >> Nå er v noden vi ønsker å slette, og vi har to designerte barn.  << 
        else:
            u = self.findMin(v.right) # finn det minste elemente i det høyre subtreet
            v.element = u.element # v sitt element er nå det minste elementet i v´s subtre
            v.right = self.removeRek(v.right, u.element) # u har ikke et venstre subtre, da det er det minste elementet.  


        v.height = 1 + max(self.Height(v.left), self.Height(v.right))
        return self.Balance(v)
    
    def Height(self, v): # Skal returnerne hoyden av seg selv og alle subtrær.
        if v == None:
            return -1
        return v.height

    def LeftRotate(self, z): # Roter treet til venstre slik at z.right blir den nye roten.

        y = z.right
        t1 = y.left

        y.left = z
        z.right = t1

        z.height = 1 + max(self.Height(z.left), self.Height(z.right))
        y.height = 1 + max(self.Height(y.left), self.Height(y.right))

        return y
    
    def RightRotate(self, z): # Roter treet til høyre slik at z.left blir den nye roten.
        
        if z is None:
            return

        y = z.left
        t2 = y.right

        y.right = z
        z.left = t2

        z.height = 1 + max(self.Height(z.left), self.Height(z.right))
        y.height = 1 + max(self.Height(y.left), self.Height(y.right))

        return y

    def BalanceFactor(self, v): # Returnerer høydeforskjellen på v sitt høyre barn og venstre barn
        if v == None:
            return 0 # 0 = balansert tre.
        return self.Height(v.left) - self.Height(v.right) # positivt tall = venstretungt, negativt tall = høyretungt.

    def Balance(self, v):
        if self.BalanceFactor(v) < -1: # if: høyretungt
            if self.BalanceFactor(v.right) > 0:
                v.right = self.RightRotate(v.right)
            return self.LeftRotate(v)

        if self.BalanceFactor(v) > 1: # if: venstretungt
            if self.BalanceFactor(v.left) < 0:
                v.left = self.LeftRotate(v.left)
            return self.RightRotate(v)
        return v
    
def kjor():

    set = AVL()
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
                    set.root = set.remove(set.root, x)

    for s in output_liste:
        print(s)
kjor()
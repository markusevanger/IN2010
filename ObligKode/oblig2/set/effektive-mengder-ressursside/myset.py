
class Set:

    class Node:
        def __init__(self, x):
            self.value = x
            self.right = None
            self.left = None
            # self.parent = None 

    def __init__(self):
        self.root = None
    
    
    # Rekursivt finner frem til tom node på riktig None type løvnode og setter til ny Node(x)
    def insert(self, node, x): # O(log(n))

        # Vi har nådd løvnoden vi skal sette inn i / treet er tomt. 
        if node == None:
            node = self.Node(x)
        
        else: 
            if node.value < x:
                self.insert(node.left, x)
            elif node > x: 
                self.insert(node.right, x)
            # else er x = node.value, og vi trenger ikke sette inn.
        
    def remove(self, node, x):
        if node == None:
            print("Fant ikke en node", x)
            return
        else:
            
            if node.left < x: 

    



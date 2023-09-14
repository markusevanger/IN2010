
class Teque:
    
    class Node:
        def __init__(self, x):
            self.value = x
            self.neste = None
            self.forrige = None

        def __str__(self):
            return str(self.value)

    class Deque:
        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0
        
        def __len__(self):
            return self.size

        def push_front(self, v):
            if self.head == None:
                self.head = v
                self.tail = v
            else: 
                self.head.forrige = v
                v.neste = self.head
                self.head = v
            self.size+=1
        
        def push_back(self, v):
            if self.tail == None: 
                self.head = v
                self.tail = v
            else:
                self.tail.neste = v
                v.forrige = self.tail
                self.tail = v
            self.size += 1
    
    # >> TEQUE <<
    def __init__(self):
        self.d1 = self.Deque()
        self.d2 = self.Deque()

    def push_front(self, x):
        self.d1.push_front(self.Node(x))
         
        if len(self.d2) < len(self.d1)-1: # om det er 2 forksjell mellom d1 og d2, må vi flytte en node fra d1 til d2. 

            # Flytte peker fra slik at [y, y, x] [y] = [y, y] [x, y] 
            self.d2.push_front(self.d1.tail) # Legg til d1.tail som d2.head
            self.d1.tail = self.d1.tail.forrige # La d1.tail være det andt siste elem i d1.
            self.d1.tail.neste = None # fjern peker fra nye d1.tail -> d2.head
            self.d2.head.forrige = None
    
            self.d1.size -= 1
    
    def push_back(self, x):
        self.d2.push_back(self.Node(x))
        # print("D1:", len(self.d1), " D2:", len(self.d2))
        if len(self.d1) < len(self.d2)-1: # da må vi flytte en node fra d2 til d1.
            print("balaneserer...", x) 
            self.d1.push_back(self.d2.head)
            self.d2.head = self.d2.head.neste
            self.d2.head.forrige = None
            self.d1.tail.neste = None

            self.d2.size -= 1
    
    def push_middle(self, x):
        
        self.d1.push_back(self.Node(x))
        if len(self.d2) < len(self.d1)-1: # om det er 2 forksjell mellom d1 og d2, må vi flytte en node fra d1 til d2. 
            # Flytte peker fra slik at [y, y, x] [y] = [y, y] [x, y] 
            self.d2.push_front(self.d1.tail) # Legg til d1.tail som d2.head
            self.d1.tail = self.d1.tail.forrige # La d1.tail være det andt siste elem i d1.
            self.d1.tail.neste = None # fjern peker fra nye d1.tail -> d2.head
            self.d2.head.forrige = None
    
            self.d1.size -= 1

    def get(self, i):

        i = int(i)
        if i > len(self.d1):
            n = self.d2.head
            teller = len(self.d1)
            while teller < i-1:
                n = n.neste
                teller+=1
            print(n)
        else:
            n = self.d1.head
            teller = 0
            while teller < i-1:
                n = n.neste
                teller+=1
            print(n)
                


            
        
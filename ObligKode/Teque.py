

class Node: 
    def __init__(self, x):
        self.verdi = x
        self.next = None

    def __str__(self):
        return str(self.verdi)

class Teque:

    def __init__(self):
        self.head = None
        self.middle = None
        self.tail = None
        self.size = 0

    def push_back(self, x):
        x = Node(x)

        if self.tail == None: # første push
            self.first_push(x)
        else:
            self.tail.next = x
            self.tail = x
        self.size += 1
    

    def push_front(self, x):
        x = Node(x)

        if self.head == None:
            self.first_push(x)
        else:
            x.next = self.head
            self.head = x
        self.size += 1


    def push_middle(self, x):
        x = Node (x)

        if self.head == None:
            self.first_push(x)
        else:

            n = self.head

            middle = (self.size)//2
            for i in range(middle-1):
                n = n.next
            x.next = n.next
            n.next = x

        self.size += 1

    def get(self, index):
        n = self.head
        for i in range(index-1):
            n = n.next
        print(n)

    def first_push(self, x):
        self.head = x
        self.middle = x
        self.tail = x

    def hent_content(self):
        s = ""
        n = self.head
        for i in range(self.size):
            s += (s(n.verdi) + ", ")
        return s


def main():

    teque = Teque()

    for n in range(int(input())): # n = antall kommandoer. 
        S = input().split(" ") # push_back, push_front, push_middle, get

        x = int(S[1])
        S = S[0]

        if S == "push_back":
            teque.push_back(x)

        elif S == "push_front":
            teque.push_front(x)

        elif S == "push_middle":
            teque.push_middle(x)

        elif S == "get":
            teque.get(x)

    print("-----")
    print(teque.hent_content())


main()
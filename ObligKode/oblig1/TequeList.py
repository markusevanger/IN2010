


class TequeList:

    def __init__(self):
        self.teque = []
    
    def __len__(self):
        return len(self.teque)

    def push_back(self, x):
        self.teque.append(x)
    def push_front(self, x):
        self.teque.insert(0, x)
    def push_middle(self, x):
        self.teque.insert((len(self.teque)+1) // 2, x)
    def get(self, i):
        print(self.teque[int(i)])

    def hent(self, i):
        return self.teque[int(i)]
    def __str__(self):
        lst = ""
        for w in self.teque:
            lst += w
            lst += ", "
        return lst


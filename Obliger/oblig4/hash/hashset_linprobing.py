

class HashSet:
    def __init__(self):
        self.size = 0
        self.ls_max = 1
        self.ls = [None]

    def __str__(self):
        for i in self.ls:
            print(i)
        return ""

    def __len__(self):
        return len(self.ls)

    def insert(self, key):
        # Om self.size er >75% av N (ls_max)
        if (self.size / self.ls_max) >= 0.75:
            self.rehash()

        if not self.contains(key):
            index = self.keyTilIndex(key)  # finn hash key til en index.

            # gå frem i listen, til det ikke lenger er en kollisjon
            while self.ls[index] != None:
                index += 1
                if index == self.ls_max:
                    index = 0
            # Skal aldri evig while løkke da vi sjekker at det er nok plass før while løkken.

            self.ls[index] = key
            self.size += 1

    # Dobbler størrelsen av interne listen.
    def rehash(self):

        self.ls_max = self.ls_max * 2
        ny_ls = [None] * self.ls_max

        gm_ls = self.ls
        self.ls = ny_ls
        self.size = 0

        for i in range(len(gm_ls)):
            if gm_ls[i] != None:
                self.insert(gm_ls[i])

    def contains(self, key):
        index = self.keyTilIndex(key)
        start_index = index
        while self.ls[index] != key:
            index = (index + 1) % self.ls_max

            if index == start_index:  # om vi rundet hele ls.
                return False

        return True

    def remove(self, key):
        if self.contains(key):
            
            index = self.keyTilIndex(key)
            while self.ls[index] != key:
                index = (index + 1) % self.ls_max
            
            self.ls[index] = None
            self.size -= 1
            self.tett_hull(index)

        return None

    def tett_hull(self, index_for_hull):

        lete_index = index_for_hull
        while self.ls[lete_index] != None:
            lete_index-=1

            key_paa_index = self.ls[lete_index]
            if self.keyTilIndex(key_paa_index) == index_for_hull:
                self.ls[index_for_hull] = key_paa_index
                self.ls[lete_index] = None
                self.tett_hull(lete_index)
 
    def size(self):
        return self.size

    def keyTilIndex(self, key):
        h = 0
        for c in key:
            h = 31 * h + ord(c)  # ord() returnerer ascii verdien til c

        return h % self.ls_max


def main():
    hs = HashSet()
    for _ in range(int(input())):
        inp = input().strip().split(" ")

        if inp[0] == "size":
            print(hs.size)
        elif inp[0] == "insert":
            hs.insert(inp[1])
        elif inp[0] == "remove":
            hs.remove(inp[1])
        elif inp[0] == "contains":
            print(hs.contains(inp[1]))

main()

import array

class HashSet:
    def __init__(self):
        self.ls = array()

    def __len__(self):
        return len(self.ls)
    
    def insert(self, key):

        index = self.keyTilIndex(key)
        self.ls[index] = key
        print(index)


    def keyTilIndex(self, key):
        h = 0
        for c in key:
            h = 31 * h + ord(c) # ord returnerer ascii verdien til c
        return h % len(self)


def main():
    hs = HashSet()
    liste = ["Hei", "Jeg", "Heter", "Markus"]
    for s in liste:
        hs.insert(s)
        print("Satt inn `", s, "` lengde:", len(hs))




main()
from visualize_hash import create_hash_viz


class HashSet:
    def __init__(self):
        self.ls = [None] 
        self.size = 0
    
    def __str__(self):
        for i in self.ls:
            print(i)
        return ""
    
    def __len__(self):
        return len(self.ls)
    
    def insert(self, key):
        
        if self.size == len(self.ls): # om vi har nådd lengden av ls
            #print(f"Size: {self.size} | len: {len(self.ls)}")
            self.resize(key)
    
        if not self.contains(key):
            index = self.keyTilIndex(key)
            if self.ls[index] != None:
                self.ls[index].append(key)
            else:
                self.ls[index] = [key]
            self.size += 1
            
        
    # Dobbler størrelsen av interne listen. 
    def resize(self, key):
        ny_ls = [None] * (len(self.ls)*2)
        gm_ls = self.ls
        self.ls = ny_ls
        self.size = 0

        for i in range(len(gm_ls)):
            if gm_ls[i] != None: # Burde fjernes om vi implementerer lineaer probing. 
                for key in gm_ls[i]:
                    self.insert(key)
        self.ls = ny_ls



    def contains(self, key):
        keyIndex = self.keyTilIndex(key)
        if self.ls[keyIndex] is not None:
            return key in self.ls[keyIndex]
        return False 
    
    def remove(self, key):
        if self.contains(key):
            self.ls[self.keyTilIndex(key)].remove(key)
            self.size -= 1
    
    
    def size(self):
        return self.size

 
    def keyTilIndex(self, key):
        h = 0
        for c in key:
            h = 31 * h + ord(c) # ord returnerer ascii verdien til c
        return h % len(self)

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


    
    


    #create_hash_viz(hs.ls)


def lagListeAvOrdFil(filnavn):
    
    ls = []
    t = 0
    lengde_teller = 0
    with open (filnavn, "r") as f:
        for linje in f:
                ls.append(linje.strip())
        return ls

main()

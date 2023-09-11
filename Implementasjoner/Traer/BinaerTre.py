class Node:

    def __init__(self, x):
        self.element = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.element)

class BinaerTre:

    def __init__(self):
        self.root = None
    
    def Insert(self, v, x):
        if v == None:
            v = Node(x)
        elif v.element > x:
            v.left = self.Insert(v.left, x)
        elif v.element < x:
            v.right = self.Insert(v.right, x)
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

    def test(self):
        print("rot: ", self.root)
        print("left: ",  self.root.left)
        print("right: ", self.root.right)

def main():
    tre = BinaerTre()
    
    tre.root = tre.Insert(None, 10)
    tre.Insert(tre.root, 5)
    tre.Insert(tre.root, 15)

    print(os.environ["PATH"])
    # visualize_binary_tree(tre.root)
    

main()
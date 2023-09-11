import pygraphviz as pgv
import random

class Node:
    def __init__(self, key):
        self.element = key
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def visualize(self, start, graph):
        if start is not None:
            graph.add_node(start.element)
            if start.left:
                graph.add_edge(start.element, start.left.element)
                self.visualize(start.left, graph)
            if start.right:
                graph.add_edge(start.element, start.right.element)
                self.visualize(start.right, graph)

    def insert(self, v, x):
        if v == None:
            v = Node(x)
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


# binary tree
b = BinaryTree()
b.insert(None, 10)

for i in range(0, 20):
    b.insert(b.root, random.randint(0, 100))


# directed graph
G = pgv.AGraph(strict=False, directed=True)

# visualize method
b.visualize(b.root, G)


# tegn
G.layout(prog='dot')
G.draw('binary_tree.png')
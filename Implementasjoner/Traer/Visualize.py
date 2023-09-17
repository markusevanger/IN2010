import pygraphviz as pgv


# Tar imot et tre og tegner det med "pygraphviz"
# Lagrer bilde som "tree.png"


def visualize(tre):

    # directed graph
    G = pgv.AGraph(strict=False, directed=True)
    visualizeRekursiv(tre.root, G)

    G.layout(prog='dot') # tegn
    G.draw('tree.png')

def visualizeRekursiv(start, graph):
    if start != None:
        graph.add_node(start.element, start.height)
        if start.left:
            graph.add_edge(start.element, start.left.element)
            visualizeRekursiv(start.left, graph)
        if start.right:
            graph.add_edge(start.element, start.right.element)
            visualizeRekursiv(start.right, graph)

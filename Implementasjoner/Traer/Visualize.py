import graphviz as pgv


# Tar imot et tre og tegner det med "pygraphviz"
# Lagrer bilde som "tree.png"


def visualize(tre):

    # directed graph
    G = pgv.Digraph(strict=False, format="png")
    visualizeRekursiv(tre.root, G)
    G.render()

def visualizeRekursiv(start, graph):
    if start != None:
        graph.node(str(start.element))
        if start.left:
            graph.edge(str(start.element), str(start.left.element))
            visualizeRekursiv(start.left, graph)
        if start.right:
            graph.edge(str(start.element), str(start.right.element))
            visualizeRekursiv(start.right, graph)

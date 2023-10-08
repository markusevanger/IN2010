import graphviz as gv


# Tar imot et tre og tegner det med "pygraphviz"
# Lagrer bilde som "tree.png"


def visualize(tre):

    # directed graph
    G = gv.Digraph()
    add_tree_nodes_edges(G, None, tre.root)
    G.render("tree", format="png")

# Define a recursive function to add nodes and edges for a tree
def add_tree_nodes_edges(G, parent_node, node):
    if node is None:
        return

    # Add the current node
    G.node(str(node.element))

    # Add the edge from the parent to the current node
    if parent_node is not None:
        G.edge(str(parent_node.element), str(node.element))

    # Recursively add nodes and edges for the left and right subtrees
    add_tree_nodes_edges(G, node, node.left)
    add_tree_nodes_edges(G, node, node.right)


import graphviz

def tegn_dict_repr_graf(G, rot):
    
    dot = dot = graphviz.Digraph(format='png')
    
    for node, neighbors in G.items():
        dot.node(node)  # Add a node for the current node
        for neighbor in neighbors:
            dot.edge(node, neighbor)  # Add an edge to each neighbor
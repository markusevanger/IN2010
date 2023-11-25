from graphviz import Graph

def create__wgraph_image(G):
    dot = Graph(format='png', engine="sfdp", graph_attr={'strict': 'true'})

    V, E, w = G
    seen_edges = set()
    
    for node in V:
        dot.node(node)
        for edge in E[node]:
            if (edge, node) not in seen_edges:
                dot.edge(node, edge, label=str(w[(node, edge)]))
                seen_edges.add((node, edge))
    
    # Render the graph to an image file
    dot.render(filename='weigthed_graph_image')  # This will create 'graph_image.png' and open it in the default image viewer


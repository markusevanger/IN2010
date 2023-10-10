from graphviz import Graph

def create_graph_image(graph):
    dot = Graph(format='png', graph_attr={'layout': 'neato', 'strict': 'true'})

    # Add nodes and edges to the graph
    added_edges = set()  # To keep track of added edges
    for node, neighbors in graph.items():
        dot.node(node)
        for neighbor in neighbors:
            # Check if the edge has already been added (in reverse direction)
            if (neighbor, node) not in added_edges:
                dot.edge(node, neighbor)
                added_edges.add((node, neighbor))

    # Render the graph to an image file
    dot.view(filename='graph_image')  # This will create 'graph_image.png' and open it in the default image viewer

if __name__ == "__main__":
    graph = {
        "A": ["B", "C", "D"],
        "B": ["A", "C"],
        "C": ["A", "B", "D", "F"],
        "D": ["A", "C", "E"],
        "E": ["D", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }

    create_graph_image(graph)

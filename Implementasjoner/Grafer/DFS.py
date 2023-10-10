from VisualizeGraph import create_graph_image

def main():
    graf = {
        "A": ["B", "C", "D"],
        "B": ["A", "C"],
        "C": ["A", "B", "D", "F"],
        "D": ["A", "C", "E"],
        "E": ["D", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }
    create_graph_image(graf)


main()
from graphviz import Graph

def create_graph_image(skuespillere, kanter, film_relasjoner):
    dot = Graph(format='png', graph_attr={'patchwork': 'patchwork', 'strict': 'true'})

    # plasser alle i graf bilde
    for v in skuespillere:
        dot.node(v.navn)
    
    # lag alle koblinger med film tittel som label på hver relasjon
    for v in skuespillere:
        for kant in kanter[v]:
            film = film_relasjoner[(v, kant)]
            dot.edge(v.navn, kant.navn, label=(film.tittel + ", " +  film.rating))

    # Render the graph to an image file
    #dot.view(filename='graph_image')  # This will create 'graph_image.png' and open it in the default image viewer

if __name__ == "__main__":
    testgraf = {
        "A": ["B", "C", "D"],
        "B": ["A", "C"],
        "C": ["A", "B", "D", "F"],
        "D": ["A", "C", "E"],
        "E": ["D", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }

    # create_graph_image(testgraf)

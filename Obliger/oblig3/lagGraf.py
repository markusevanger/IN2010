from vizualize import create_graph_image

class Film:

    def __init__(self, film_id, tittel, rating):
        self.id = film_id
        self.tittel = tittel
        self.rating = rating

    def __str__(self):
        return f"{self.tittel} ({self.rating})"
    
    
class Actor:
    def __init__(self, actor_id, navn, filmerSpiltI):
        self.id = actor_id
        self.navn = navn
        self.filmer = filmerSpiltI
    def __str__(self):
        return f"{self.navn}"


# Ta imot tsv fil med filmer og opprett film objekter for hver linje.
def les_filmer(filmer_fil):
    filmDict = {}
    f = open(filmer_fil, "r", encoding="utf-8")
    for linje in f:
        linje = linje.split("\t")
        filmDict[linje[0]] = Film(linje[0], linje[1], linje[2])

    return filmDict

# Ta imot tsv fil med actors og opprett film objekter for hver linje. 
def les_actors(actors_fil):
    li = []
    f = open(actors_fil, "r",  encoding="utf-8")
    for linje in f:
        linje = linje.split("\t")
        li.append(Actor(linje[0], linje[1], linje[2:]))
    return li

def bygg_graf(filmer, actors):
    
    # Bruker dict representasjon av graf
    kanter = {} 

    teller = 0
    for a in actors:

        teller += 1
        print(str(round(teller/len(actors)*100, 2)) + "% ferdig")
        for b in actors:
            if a != b:
                for film in a.filmer:
                    if film in b.filmer:
                        kanter[a] = b            

    return kanter

def main():
    filmer = les_filmer("six-degrees-of-imdb-ressursside-main/marvel_movies.tsv")
    actors = les_actors("six-degrees-of-imdb-ressursside-main/marvel_actors.tsv")

    graf = bygg_graf(filmer, actors)
    # create_graph_image(graf)

    print("Noder:", len(graf))

    ant_edges = 0
    for a in graf:
        ant_edges += len(graf)
    print("Edges:", ant_edges)





main()
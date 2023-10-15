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
    
    def __repr__(self):
        return self.__str__()


# Ta imot tsv fil med filmer og opprett film objekter for hver linje.
def les_filmer(filmer_fil):
    filmDict = {}
    print("Begynner aa lese:", filmer_fil)
    f = open(filmer_fil, "r", encoding="utf-8")
    for linje in f:
        linje = linje.strip().split("\t")
        filmDict[linje[0]] = Film(linje[0], linje[1], linje[2])

    f.close()
    print("Ferdig aa lese:", filmer_fil)
    return filmDict

# Ta imot tsv fil med actors og opprett film objekter for hver linje. 
def les_actors(actors_fil):
    li = []
    print("Begynner aa lese:", actors_fil)
    f = open(actors_fil, "r",  encoding="utf-8")
    for linje in f:
        linje = linje.strip().split("\t")
        li.append(Actor(linje[0], linje[1], linje[2:]))
    print("Ferdig aa lese:", actors_fil)
    f.close()
    return li

def finn_sammenhenger(filmer, actors):

    
    
    # Bruker dict representasjon av graf
    skuespillere = set() 
    kanter = {} # dict med nøkkel skuespiller, som  
    film_relations = {} # ha en edge (u,v) -> film objekt som kobler dem sammen

    teller = 0 # kun for å vite progress, fordi algoritmen er så treg. 
    for a in actors:
        print(str(round(teller/len(actors)*100, 2)) + "% ferdig")
        teller += 1
        skuespillere.add(a)
        kanter[a] = set()
        for b in actors:
            if a != b:
                for film in a.filmer:
                    if film in b.filmer:
                        kanter[a].add(b)
                        film_relations[(a, b)] = filmer[film]           

    return skuespillere, kanter, film_relations
            
def main():

    filmer = les_filmer("six-degrees-of-imdb-ressursside-main/marvel_movies.tsv")
    actors = les_actors("six-degrees-of-imdb-ressursside-main/marvel_actors.tsv")
    skuespillere, kanter, film_relasjoner = finn_sammenhenger(filmer, actors)

    if kanter < 1000: # graphviz kræsjer om det er for langt / 1000 er nok for å illustrere marvel. 
        create_graph_image(skuespillere, kanter, film_relasjoner)

    print("Noder:", len(skuespillere))

    ant_edges = 0
    for a in kanter:
        ant_edges += len(kanter[a])
    print("Edges:", ant_edges)


main()
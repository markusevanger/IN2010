from vizualize import create_graph_image
from collections import deque

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
def les_actors(actors_fil, registrerte_filmer):
    li = []
    print("Begynner aa lese:", actors_fil)
    f = open(actors_fil, "r",  encoding="utf-8")
    for linje in f:
        linje = linje.strip().split("\t")
        li.append(Actor(linje[0], linje[1], [film for film in linje[2:] if film in registrerte_filmer]))
    print("Ferdig aa lese:", actors_fil)
    f.close()
    return li

def finn_sammenhenger(filmer, actors):

    print(f"Finner sammenhenger mellom {len(actors)} skuespillere og {len(filmer)} filmer.")
    # Bruker dict representasjon av graf
    skuespillere = set() 
    kanter = {} # dict med nøkkel skuespiller og verdi set av skuespillere som har spilt i samme film
    film_relations = {} # ha en edge (u,v) -> film objekt som kobler dem sammen

    teller = 0 # kun for å vite progress, fordi algoritmen kan være treg på større filer. 
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




def raskeste_vei(G, s, t): # bredde først

    print(f"Finner raskeste rute fra {s.navn} => {t.navn}")

    parents = bgs_shortest_paths_from(G, s)
    v = t
    path = []

    if t not in parents: # om t ikke ble funent.
        return path

    while v:
        path.append(v)
        v = parents[v]
    return path[::-1]

def bgs_shortest_paths_from(G, s):
    _, E, filmer = G
    parents = {s : None}
    queue = deque([s])

    while queue:
        u = queue.popleft()
        for v in E[u]:
            if v not in parents:
                parents[v] = u
                queue.append(v)
    return parents



def chilleste_vei(): # djikstra. (?)
    pass

def main():

    filmer = les_filmer("six-degrees-of-imdb-ressursside-main/movies.tsv")
    actors = les_actors("six-degrees-of-imdb-ressursside-main/actors.tsv", filmer)
    skuespillere, kanter, film_relasjoner = finn_sammenhenger(filmer, actors)
    
    # gjøre om str til actor objekter. 
    start = "Donald Glover"
    slutt = "Jeremy Irons"

    s = [a for a in actors if a.navn == start][0]
    t = [a for a in actors if a.navn == slutt][0]

    raskeste = raskeste_vei((skuespillere, kanter, film_relasjoner), s, t)
    
    print()
    print("==== RASKESTE VEI ====")
    for i in range(len(raskeste)-1):
        print(f"===> {raskeste[i]} ===> {film_relasjoner[(raskeste[i], raskeste[i+1])]} ===> {raskeste[i+1]}")

    if len(kanter) < 1000: # graphviz kræsjer om det er for langt / 1000 er nok for å illustrere marvel. 
        create_graph_image(skuespillere, kanter, film_relasjoner)

    print("Noder:", len(skuespillere))

    ant_edges = 0
    for a in kanter:
        ant_edges += len(kanter[a])
    print("Edges:", ant_edges)


main()
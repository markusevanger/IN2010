# from vizualize import create_graph_image

class Film:

    def __init__(self, film_id, tittel, rating):
        self.id = film_id
        self.tittel = tittel
        self.rating = rating

    def __str__(self):
        return f"{self.tittel} ({self.rating})"
    
class Actor:
    def __init__(self, actor_id, navn, filmerSpiltI, filmerDict):
        self.id = actor_id
        self.navn = navn
        self.filmer = []

        for f in filmerSpiltI:
            f = f.strip() # siste film id har \n bak seg.
            if f in filmerDict:
                self.filmer.append(filmerDict[f]) 
    
    def __str__(self):
        print(f"{self.navn} har spilt i {len(self.filmer)} filmer:")
        for f in self.filmer: 
            print(f"- {f}")
        return ""

def lesFilmer(filmer_fil):
    filmDict = {}
    f = open(filmer_fil, "r")
    for linje in f:
        linje = linje.split("\t")
        filmDict[linje[0]] = Film(linje[0], linje[1], linje[2])

    return filmDict

def lesActors(actors_fil, filmer):
    li = []
    f = open(actors_fil)
    for linje in f:
        linje = linje.split("\t")
        li.append(Actor(linje[0], linje[1], linje[2:], filmer))
    return li

def main():
    filmer = lesFilmer("six-degrees-of-imdb-ressursside-main/marvel_movies.tsv")
    actors = lesActors("six-degrees-of-imdb-ressursside-main/marvel_actors.tsv", filmer)

    for a in actors:
        print(a)

main()
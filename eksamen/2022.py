


"""
OPPVARMING

a) Hva er en algoritme:
    - En algorimte er et sett av instrukser som terminerer med et endelig input. En algoritme tar gjerne imot et input, gjør noe med input og returnerer et output basert på inputtet. 

b) Hva er en datastruktur:
    - En datastruktur er en måte å holde data på. Med andre ord er det hvordan vi velger å organisere dataen vår i datamaskinen, og hvordan vi kan endre, og hente data.

    

LITT AV HVERT:
(a) Binære trær består av noder som har opptil to barn.
    - Sant

(b) Hvis en algoritme bruker O(n) antall steg sier vi den har lineær kjøretidskompleksitet.
    - Sant

(c) Kjøretidskompleksitet til Mergesort er O(n · log(n)).
    - Sant

(d) Det er umulig å sjekke om et array er sortert i O(n).
    - Usant

(e) Binærsøk på arrayer er betydelig raskere enn binærsøk på lenkede lister.
    - Sant

(f ) Kjøretidskompleksitet sier noe om hvor mange steg en algoritme bruker i forhold til størrelsen på input.
    - Sant

(g) Dersom en algoritme har bedre kjøretidskompleksitet enn en annen algoritme, så vil den alltid bruke
færre steg uansett størrelse på input.
    - Usant

(h) Huffman-koding brukes for å komprimere data.
    - Sant

(i) Rotnoden av et tre er den eneste noden som ikke har en forelder.
    - Sant

(j) En graf med n noder kan ikke har mer enn n kanter
    - Usant

(^ alt riktig)


"""

######################################################################

"""
GRAFEGENSKAPER

Grafen er sammenhengende
    - Begge

Grafen er 2-sammenhengende
    - Ingen

Grafen er et tre
    - G1

Grafen har mer enn to seprasjonsnoder
    - (tidl. svar: Begge) G1 <--- leste feil, ~mer~ enn 2. ikke 2 eller mer. MINST 3 SEPNODER.

Grafen har to (forskjellige) stier fra B til F
    - G2

Grafen har to komponenter
    - Ingen

Grafen er rettet
    - Ingen


Grafen inneholder en sykel
    - G2


Grafen blir ett tre hvis vi fjerner én kant
    - G2


Grafen er en enkel graf
    - (tidl. svar: G1) Begge <--- Enkel graf er bare en graf som ikke har kanter til seg selv, eller flere  til samme node.

    
"""

######################################################

"""
BALANSERTE SØKETRÆR
    
(a) Hvilket av AVL-trærne ovenfor får man hvis man legger inn tallene 1 til 5 i rekkefølgen 2, 4, 3, 1, 5? Oppgi
svaret som et tall mellom 1 og 6.
    - 5 

(b) Hvor mange av trærne ovenfor kan fargelegges som et rød-svart tre?
    - Alle

(c) Hvis vi legger til 6 i alle AVL-trærne ovenfor, i hvilke trær vil det forekomme rotasjoner? Oppgi svaret
som summen av alle trærne det gjelder. Altså, hvis det kun forekommer rotasjoner i det første treet, er
svaret 1, og hvis det forekommer rotasjoner i alle trærne, er svaret 21 (fordi 1 + 2 + 3 + 4 + 5 + 6 = 21).
    - 2 + 4 + 5 = 11

"""

###############################################################################################

"""
LITT OM PRIORITETSKØER OG BINÆRE HEAPS:

Med heap mener vi arrayer som representerer binære min-heaps.

(a) En array med n elementer kan gjøres om til en heap i O(n).
    - (sant) !!

(b) En min-heap blir en max-heap ved å reversere arrayet.
    - Usant


(c) Alle elementer på dybde d i en heap er mindre enn alle elementer på dybde d + 1.
    - (tidl. svar: Sann) Usann <-- Fordi søsken kan vær vidt forskjellig og har ingen sammenheng annen enn innsetningstid


(d) Innsetting i en heap med n elementer er O(log(n)) i verste tilfelle.
    - Sann

(e) Et AVL-tre kan brukes som en prioritetskø med samme kjøretidskompleksitet som en heap.
    - Sann ..........

(f ) Nodene langs en sti fra rotnoden til en løvnode i en heap er ordnet fra minst til størst.
    - Sann

(g) Dersom vi bytter plass på to søskennoder i en heap, er det fremdeles en heap.
    - Sann

(h) En prioritetskø med konstant tid på alle operasjoner ville gjort at Dijkstra hadde kjøretidskompleksitet
O(|V | +|E|).
    - Sann

(i) Man kan finne det største elementet i en min-heap i O(log(n)).
    - Usann

(j) I en heap ligger over halvparten av elementene på de to dypeste nivåene
    - Sann

"""

################################################################################################################

"""

KJØRETID PÅ GRAFALGORIMTER:

For hver grafalgoritme, kryss av på den (laveste) korrekte kjøretidskompleksiteten.

O(1) 
O(|V|+ |E|): DFSFull, TopSort
O((|V| + |E|) * log(|V|)) - Prim
O(|V| * |E|): Bellman Ford


"""

#################################################################################################################

"""
LINEAR PROBING

a)

Tomt array med size: 10:

[ __, __, __, __, __, __, __, __, __, __ ]
[ 00, 01, 02, 03, 04, 05, 06, 07, 08, 09 ]

Hashfunksjonen du skal bruke er h(k, N) = k mod N, som for dette eksempelet blir det samme som
h(k, 10) = k mod 10. Altså hasher et tall til sitt siste siffer.

Bruk linear probing til å sette inn disse tallene i den gitte rekkefølgen:
21, 54, 82, 10, 20, 44

[ 10, 21, 82, 20, 54, 44, __, __, __, __ ]
[ 00, 01, 02, 03, 04, 05, 06, 07, 08, 09 ]


b)

Forklar kort hvordan algoritmen for innsetting ved linear probing fungerer, og skisser algoritmen med
pseudokode. Du kan anta at arrayet i input ikke er fullt, og at du har en hashfunksjon h slik at h(k, N) gir
et tall mellom 0 og N - 1 for en vilkårlig nøkkel k. Ledig plass i arrayet er indikert ved null

Linear probing går ut på å finne indeksen (i) k hasher til, deretter om i er tatt må vi loope gjennom array til vi finner en ledig plass. 
Om nøkkelen allerede eksisterer overskriver vi nøkkelens gamle v. 

"""

#Input: array A of size N, a key k and value v
#Output: A containing (k, v)
def LinearProbingInsert(A, k, v):
    
    i = h(k, N)

    while A[i] is not None:
        if key in A[i] is k:
            break
        i = (i + 1) % N

    A[i] = (k, v)



#######################################################################################################################
"""
GARBAGE COLLECTION

    G = (V, E), rettet graf av alle objekter


"""

# IN: Objekt graf G = (V, E) og en mengde med R objekter.
# OUT: Frigjør alle objekter det ikke finnes en referanse til

def GarbageCollect(G, R):
    
    visited = set()
    
    for v in R:
        if v not in visited:
            DFSVisit(G, R, u, visited)

    for v in V:
        if v not in visited:
            free(G, v) 

    return G


def DFSVisit(G, R, u, visited): 
    
    visited.add(u)

    for (u, v) in E:
        if v not in visited:
            DFSVisit(G, R, v, visited)



########################################################################################################
"""
AUTOCOMPLETE

Strategi 1 bruker minimalt minne, da den kun lagrer hver nødvendige bokstav i minne, og dermed er den mest effektive måten vi kan lagre dataen med tanke på minne.
Men siden vi ønsker å bruke treet til å hente alle mulige ord basert på prefixen som er foran, krever det traversering og bygging av hvert mulige ord. 

Strategi 2, krever at vi har alle mulige ord, og alle prefix lastet inn i minne, og er dermed mindre effektiv minnebruk. Fordelen med denne strategien er at vi
bruker hashing, og hashen returnerer listen i trenger - og er dermed enormt rask til bruken vår.

Begge vil jeg si er nokså likt balansert med tanke på hvilke kompromisser som gjøres, og hvilken implementasjon som blir brukt, krever en forståelse av hvor 
løsningen blir brukt og på hvilken hardware. 



"""
########################################################################################################

"""
BUCKET QUEUE:

a) Basert på beskrivelsen så passer en minheap godt her, da den allerede støtter funksjonene Insert, RemoveMin.

"""
#b)
# IN: En bucket queue Q med prioriteter fra 0 til N - 1 og et element x med prioritet p
# OUT: Q med x satt inn med prioritet p
def Insert(Q, x, p):

    i = len(Q)-1
    Q[i] = (p, x)

    # bubbleUp
    while priority of Q[parentOf(i)] > p and i > 0:
        Q[parentOf(i)], Q[i] = Q[i], Q[parentOf(i)]
        i = parentOf(i)

    return Q

def RemoveMin(Q):

    k = Q[0]
    Q[0] = Q.pop() 

    # bubbleDown
    i = 0
    while leftOf(i) < len(Q):
        
    
    if priority of Q[i] > priority of 
        

def parentOf(i):
    return (i-1)//2
def leftOf(i):
    return 2*i+1
def rightOf(i):
    return 2*i+2





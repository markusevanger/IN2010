

def insertionSort(A): # Har også kvadratisk kjøretid. 

    # i insertion sort "dytter" vi den minste verdien alltid lengst mulig til venstre.
    
    n = len(A)
    for i in range(1, n): # iterer fra og med 1 til og med index n
        j = i # j = verdi som sier hvor vi er i listen
        while j > 0 and A[j-1] > A[j]: # imens verdien til venstre for j er større enn j (eller j = 0, og det ikke er noe til venstre)
            A[j-1], A[j] = A[j], A[j-1] # bytt posisjoner 
            j = j - 1 #flytt j lenger bak. 
    return A

def main():
    usortertListe = [4, 9, 2, 1, 5, 3, 6, 8, 7]

    print("Her er den usorterte listen: ", usortertListe)
    print("Her er en insertion sortert liste: ", insertionSort(usortertListe))

main()
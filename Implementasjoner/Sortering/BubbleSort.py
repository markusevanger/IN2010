

def bubbleSort(A): # Kvadratisk kjøretid. 
    
    n = len(A)

    for i in range(n-1): # Itererer gjennom alle elementer
        for j in range(n - i - 1): # Iterer gjennom elementene "foran" elementet som blir iterert fra forrige loop
            if A[j] > A[j + 1]: # Om elementet er større enn det foran deg, flytter byttes posisjon.  
                A[j], A[j + 1] = A[j + 1], A[j] # Swap posisjon

    return A

def main():
    usortertListe = [4, 9, 2, 1, 5, 3, 6, 8, 7]

    print("Her er den usorterte listen: ", usortertListe)
    print("Her er en bubble sortert liste: ", bubbleSort(usortertListe))

main()


def selectionSort(A): # Har også kvadraktisk kjøretid'

    # Iterer gjennom listen og bytt minste tall i resten av listen med deg selv. 
    
    # Selection Sort er forholdsvis lik bubblesort, men gjør bytter av posisjon mye sjeldnere enn bubblesort. 
    # Da sparer vi en del ressurser.
    
    n = len(A)

    for i in range(n): # Iterer gjennom listen
        k = i # k = minste tall, settes som første
        for j in range(i + 1, n): # iterer gjennom resten av listen
            if A[j] < A[k]: # om et tall i resten av listen er mindre enn k:
                k = j # j er nå det minste tallet i resten av listen. 
        if i != k: #bytt posisjon om vi fant et mindre tall
            A[i], A[k] = A[k], A[i] 

    return A

def main():
    usortertListe = [4, 9, 2, 1, 5, 3, 6, 8, 7]

    print("Her er den usorterte listen: ", usortertListe)
    print("Her er en selection sortert liste: ", selectionSort(usortertListe))

main()
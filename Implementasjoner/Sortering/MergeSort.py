

# tar to SORTERTE arrayer og fletter dem sammen. 
def merge(A1, A2, A):
    
    i = 0
    j = 0

    # Denne while løkken iterer over begge listene og legger til det minste elemente fra en av listene. 
    while i < len(A1) and j < len(A2): 
        if A1[i] <= A2[j]: # om element i A1 er mindre elller lik A2:
            A[i + j] = A1[i] # Legg element i A1 i A. 
            i = i + 1 # Inkrementer index for A1: i.
        
        else: # Element A2 er mindre eller lik element i A1:
            A[i + j] = A2[j] # legg til element fra A2 i A
            j = j + 1 # inkrmenter indexx for A2: j. 

    # Siden while løkken over kjører til kun en av listene er blitt indeksert ferdig må vi fylle A med resten fra enten A1 eller A2
    while i < len(A1): # Kjører så lenge A1 ikke er ferdig indeksert
        A[i + j] = A1[i] # legger til i slutten av listen A
        i = i + 1

    while j < len(A2): # Kjører så lenge A2 ikke er ferdig indeksert
        A[i + j] = A2[j]
        j = j + 1

    return A 


# Tar en liste og splitter den i to, og rekursivt kaller mergeSort på hver splittet liste. 
# Listen returneres kun når lengen av listen er 1. 
def mergeSort(A): # inkl Merge har mergeSort() en kjøretids kompleksitet på: O(n*log(n))

    n = len(A)
    if n <= 1: # true når listen har blitt splittet nok til n = 1 
        return A # avslutter reksursiv løkke
    
    i = n//2 # finner midtpunktet av listen.

    # kaller rekursivt på mergeSort 
    A1 = mergeSort(A[:i]) # splicer listen i to, A[0...i-1]
    A2 = mergeSort(A[i:]) # A[i...n], Returnerer lister som er sortert med innhold. 
    return merge(A1, A2, A) # Deretter merger sorterte og usorterte lister. 


def main():
    usortertListe = [4, 9, 2, 10, 5, 3, 6, 8, 7, 1]

    print("Her er den usorterte listen: ", usortertListe)
    print("Her er en merge sortert liste: ", mergeSort(usortertListe))

main()
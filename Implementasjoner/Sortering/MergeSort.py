

# Tar to sorterte arrayer og slår dem sammen til et array, A
def merge(A1, A2, A):
    
    i = 0
    j = 0

    while i < len(A1) and j < len(A2):
        if A1[i] <= A2[j]:
            A[i + j] = A1[i]
            i = i + 1
        else:
            A[i + j] = A2[j]
            j = j + 1
    
    while i < len(A1):
        A[i + j] = A1[i]
        i = i + 1

    while j < len(A2):
        A[i + j] = A2[j]
        j = j + 1

    return A


# Tar en liste og splitter den i to, og rekursivt kaller mergeSort på hver splittet liste. 
# Listen returneres kun når lengen av listen er 1. 
def mergeSort(A):

    n = len(A)
    if n <= 1: # true når listen har blitt splittet nok til n = 1 
        return A # avslutter reksursiv løkke
    
    i = n//2 # finner midtpunktet av listen.

    # kaller rekursivt på mergeSort 
    A1 = mergeSort(A[:i]) # splicer listen i to, A[0...i-1]
    A2 = mergeSort(A[i:]) # A[i...n]
    return merge(A1, A2, A)


def main():
    usortertListe = [4, 9, 2, 10, 5, 3, 6, 8, 7, 1]

    print("Her er den usorterte listen: ", usortertListe)
    print("Her er en merge sortert liste: ", mergeSort(usortertListe))

main()
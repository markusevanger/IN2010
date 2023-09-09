

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


def mergeSort(A):

    n = len(A)

    if n <= 1:
        return A
    
    i = n//2
    A1 = mergeSort(A[:i])
    A2 = mergeSort(A[i:])
    return merge(A1, A2, A)


def main():
    usortertListe = [4, 9, 2, 10, 5, 3, 6, 8, 7, 1, 11]

    print("Her er den usorterte listen: ", usortertListe)
    print("Her er en merge sortert liste: ", mergeSort(usortertListe))

main()


def selectionSort(A):

    for i in range(len(A)):
        k = i
        for j in range(i, len(A)):
            if A[j] < A[k]:
                k = j
        if k != i:
            A[k], A[i] = A[i], A[k]
            print(A)

    return A

ls = [5, 2, 6]
selectionSort(ls)

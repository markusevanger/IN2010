def selectionSort(A):

    for i in range(len(A)-1):
        k = i
        for j in range(i, len(A)-1):
            if A[j] < A[k]:
                k = j
        if k != i:
            A[i], A[k] = A[k], A[i]
    
    return A

def main():

    A = [1, 5, 2, 8, 3, 5]
    print(A)
    print(selectionSort(A))

main()
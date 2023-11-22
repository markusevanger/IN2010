def selectionSort(A):

    for i in range(len(A)-1):
        k = i
        for j in range(i, len(A)-1):
            if A[k] > A[j]:
                k = j
        if k != i:
            A[i], A[k] = A[k], A[i]
    return A



def main():

    A = [4, 2, 1, 5]
    print(A)
    print(selectionSort(A))

main()
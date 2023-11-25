


def bubbleSort(A):

    for i in range(len(A)):
        for j in range(len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                print(A)
    return A

ls = [5, 2, 6]
bubbleSort(ls)
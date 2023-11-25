
def bubbleSort(A):

    n = len(A)
    for i in range(n):
        for j in range(n-1):
            if A[j+1] < A[j]:
                A[j], A[j+1] = A[j+1], A[j]
                print(A)

    return A

ls = [5, 2, 6, 10]
bubbleSort(ls)
def selectionSort(A):


    for i in range(len(A)):
        k = i
        for j in range(i, len(A)):
            if A[k] > A[j]:
                k = j
        if k!=i:
            A[i], A[k] = A[k], A[i]
    return A

def main():

    A = [1, 5, 2, 8, 3, 5]
    print(A)
    print(selectionSort(A))

main()
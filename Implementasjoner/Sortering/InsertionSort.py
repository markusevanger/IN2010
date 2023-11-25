
def InsertionSort(A):
    for i in range(len(A)):
        j = i 
        while j > 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
            j = j - 1
    return A


ls = [5, 3, 2, 6, 8, 9]
print(ls)
print(InsertionSort(ls))
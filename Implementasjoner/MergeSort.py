




def MergeSort(A):
    if len(A) <= 1:
        return A
   
    i = len(A)//2
    A1 = MergeSort(A[:i])
    A2 = MergeSort(A[i:])
    
    return Merge(A, A1, A2)


def Merge(A, A1, A2):
    
    i = 0
    j = 0

    while i < len(A1) and j < len(A2):
        if A1[i] > A2[j]:
            A[i+j] = A2[j]
            j+=1
        else:
            A[i+j] = A1[i]
            i += 1

    while i < len(A1):
        A[i + j] = A1[i]
        i+=1
    while j < len(A2):
        A[i + j] = A2[j]
        j+=1

    return A


ls = [5, 8, 1, 9, 3]
print(ls)
print(MergeSort(ls))

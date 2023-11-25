



def MergeSort(A):

    if len(A) <= 1:
        return A

    i = len(A)//2

    A1 = MergeSort(A[:i])
    A2 = MergeSort(A[i:])
    return Merge(A1, A2, A)

def Merge(A1, A2, A):

    i = 0
    j = 0

    while j < len(A2) and i < len(A1):
        
        if A1[i] < A2[j]:
            A[j + i] = A1[i]
            i += 1
        else:
            A[j + i] = A2[j]
            j += 1
    
    while j < len(A2):
        A[j + i] = A2[j]
        j+=1
    while i < len(A1):
        A[j+i] = A1[i]
        i+=1

    return A

ls = [5, 2, 1, 9, 3, 6, 8]
print(MergeSort(ls))
def Insert(A, x):
    i = len(A)
    A.append(x)
    

    while 0 < i and A[i] < A[ParentOf(i)]: 
        A[i], A[ParentOf(i)] = A[ParentOf(i)], A[i]
        i = ParentOf(i)

def ParentOf(i):
    return (i-1)//2
def LeftOf(i):
    return 2*i+1
def RightOf(i):
    return 2*i+2


def RemoveMin(A):

    n = len(A)
    x = A[0]
    A[0] = A.pop()
    i = 0
    
    while RightOf(i) < n-1:
        if A[LeftOf(i)] <= A[RightOf(i)]:
            j = LeftOf(i)
        else:
            j = RightOf(i)

        if A[j] > A[i]:
            break
        A[i], A[j] = A[j], A[i]
        i = j

    if LeftOf(i) < n-1 and A[LeftOf(i)] <= A[i]:
        A[i], A[LeftOf(i)] = A[LeftOf(i)], A[i]
    return x


def main():
    heap = []
    for i in range(1, 5):
        Insert(heap, i)
    print(heap)
    RemoveMin(heap)
    print(heap)

main()
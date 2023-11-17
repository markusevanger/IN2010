
def parentOf(i):
    return (i-1)//2

def leftOf(i):
    return 2*i+1
def rightOf(i):
    return 2*i+2

####

def bubbleUp(A, i):

    while i > 0 and A[parentOf(i)] > A[i]:
        A[i], A[parentOf(i)] = A[parentOf(i)], A[i]
        i = parentOf(i)
    return A

def bubbleDown(A, i):
    while rightOf(i) < len(A)-1:
        j = None
        l = leftOf(i)
        r = rightOf(i)

        if A[l] > A[r]:
            j = r
        else:
            j = l

        if A[j] > A[i]:
            break

        A[i], A[j] = A[j], A[i]
        i = j
    
    if A[leftOf(i)] < A[i]:
        A[i], A[leftOf(i)] = A[leftOf(i)], A[i]
    
    return A
###


def removeMin(A):
    A[0] = A.pop()
    A = bubbleDown(A, 0)
    return A

def insert(A, x):
    A.append(x)
    A = bubbleUp(A, len(A)-1)
    return A



def main():
    heap = [2, 4, 6, 8, 10]
    print(heap)
    print(removeMin(heap))
    print(insert(heap, 1))

main()
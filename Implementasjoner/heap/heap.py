

# Finne familie metdoer:

def parentOf(i):
    return (i-1)//2 # forelder

def leftOf(i):
    return 2*i+1 # venstre barn

def rightOf(i): # høyre barn
    return 2*i+2

def swap(A, i, k):
    A[i], A[k] = A[k], A[i]
    return A



# Modifikasjons metoder:
def insert(A, x):
    A.append(x)
    A = bubbleUp(A, len(A)-1)
    return A


def removeMin(A):
    A[0] = A.pop()
    A = bubbleDown(A, 0)
    return A


# Flytte metoder
def bubbleUp(A, i):
    while i > 0 and A[parentOf(i)] > A[i]:
        
        j = parentOf(i)
        A = swap(A, i, j)
        i = j

    return A


def bubbleDown(A, i):
    
    while rightOf(i) < len(A):
        
        j = 0
        l = leftOf(i)
        r = rightOf(i)
        if A[l] > A[i]:
            j = l
        else:
            j = r

        if A[j] > A[i]:
            break

        A = swap(A, i, j)

    if A[leftOf(i)] < A[i]:
        A = swap(A, A[leftOf(i)], i)
    
    return A



def main():

    heap = [0, 2, 4, 6, 8]
    print("Før",heap)


    print("removeMin:", removeMin(heap))

    print("Insert(10)", insert(heap, 10))


main()
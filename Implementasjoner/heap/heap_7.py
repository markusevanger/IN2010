
def parentOf(i):
    return (i-1)//2
def leftOf(i):
    return i*2+1
def rightOf(i):
    return i*2+2


def bubbleUp(A, i):

    while A[parentOf(i)] > A[i] and i > 0:
        A[i], A[parentOf(i)] = A[parentOf(i)], A[parentOf(i)]
        i = parentOf(i)
    return A

def bubbleDown(A, i):

    while rightOf(i) < len(A)-1:

        j = None
        r = rightOf(i)
        l = leftOf(i)
        if A[r] > A[l]:
            j = l
        else:
            j = r
        
        if A[j] > A[i]:
            break
        A[j], A[i] = A[i], A[j]
        i = j

    if A[leftOf(i)] < A[i]:
        A[i], A[leftOf(i)] = A[leftOf(i)], A[i]
    return A


def removeMin(A):
    A[0] = A.pop()
    A = bubbleDown(A, 0)
    return A

def insert(A, x):
    A.append(x)
    A = bubbleUp(A, len(A)-1)
    return A

def main():
    
    A = [1, 3, 5, 7, 9]
    print(insert(A, 2))
    print(removeMin(A))

main()

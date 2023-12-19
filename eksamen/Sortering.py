from emoji import emojize # pip install emoji

def BubbleSort(A): #O(n^2) guh

    n = len(A)

    for i in range(n):
        for j in range(n):
            if A[i] < A[j]:
                A[i], A[j] = A[j], A[i]
    return A

def SelectionSort(A): #O(n^2) gjør minste antall faktiske bytter.
    n = len(A)
    for i in range(n-1):
        k = i
        for j in range(i, n): # husk fra og med i til n-1
            if A[k] > A[j]:
                k = j
        if k != i:
            A[k], A[i] = A[i], A[k]
    return A

def InsertionSort(A): #O(n^2) men om den er sortert får vi O(n)
    n = len(A)
    for i in range(n):
        j = i
        while j > 0 and A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
    return A


def MergeSort(A):

    n = len(A)

    def Merge(A1, A2, A):
        
        i = 0
        j = 0
        while i < len(A1) and j < len(A2):
            if A1[i] < A2[j]:
                A[j+i] = A1[i]
                i+=1
            else:
                A[j+i] = A2[j]
                j += 1

        while i < len(A1):
            A[j+i] = A1[i]
            i+=1
        while j < len(A2):
            A[j+i] = A2[j]
            j+=1
        
        return A

    #######
    if n <= 1:
        return A
    i = n//2
    A1 = MergeSort(A[:i])
    A2 = MergeSort(A[i:])
    return Merge(A1, A2, A)


def HeapSort(A):

    n = len(A)

    def buildMaxHeap(A): # logisk i n*log(n) men er i n av magiske grunner 
        i = n//2
        while i >= 0:
            bubbleDown(A, i, n)
            i-=1
        return A

    def bubbleDown(A, i, n):
        largest = i
        left = 2* i + 1
        right = 2* i + 2
    
        if left < n and A[largest] < A[left]:
            largest, left = left, largest
        if right < n and A[largest] < A[right]:
            largest, right = right, largest
        
        if i != largest:
            A[i], A[largest] = A[largest], A[i]
            bubbleDown(A, largest, n)


    A = buildMaxHeap(A)
    i = n-1
    while i > 0:
        A[i], A[0] = A[0], A[i]
        bubbleDown(A, 0, i)
        i-=1
    return A


def QuickSort(A, low, high):

    def partition(A, low, high):
        p = A[(high+low)//2]
        A[p], A[high] = A[high], A[p]

        pivot = A[high]
        left = low
        right = high - 1

        while left <= right:
            while left <= right and A[left] <= pivot:
                left = left + 1

            while right >= left and A[right] >= pivot:
                right = right - 1

            if left < right:
                A[left], A[right] = A[right], A[left]
        A[left], A[high] = A[high], A[left]
        return left
    ################

    if low >= high:
        return A
    p = partition(A, low, high)
    QuickSort(A, low, p-1)
    QuickSort(A, p+1, high)
    return A

def main():

    A = [5, 2, 9, 4, 2, 1, 3, 6]
    print("NoSort:       ", A, emojize(":sparkles:"), "O(1)")
    print("BubbleSort:   ", BubbleSort(A), emojize(":check_mark_button:"), "O(n²)")
    print("SelectionSort:", SelectionSort(A), emojize(":check_mark_button:"), "O(n²)")
    print("InsertionSort:", InsertionSort(A), emojize(":check_mark_button:"), "O(n²)")
    print("MergeSort:    ", MergeSort(A), emojize(":check_mark_button:"), "O(n * log(n))")
    print("HeapSort:     ", HeapSort(A), emojize(":check_mark_button:"), "O(n * log(n))")
    print("QuickSort:    ", QuickSort(A, 0, len(A)-1), emojize(":check_mark_button:"), "O(n²) < O(n * log(n)")

main()
    

def bubbleSort(A):

    for i in range(len(A)):
        for j in range(len(A)):
            if i != j:
                if A[i] < A[j]:
                    A[j], A[i] = A[i], A[j]
    return A

def main():


    A = [9, 4, 3, 2, 1, 6, 8, 7, 5]
    print(A)
    print(bubbleSort(A))

main()
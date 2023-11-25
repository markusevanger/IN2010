

A = [5, 2, 10, 6]

for i in range(len(A)):
    j = i
    while j > 0 and A[j] < A[j-1]:
        A[j-1], A[j] = A[j], A[j-1]
        print(A)
        j = j -1
        
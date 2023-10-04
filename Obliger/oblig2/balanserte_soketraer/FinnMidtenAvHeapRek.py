import heapq

def FinnMidtenAvHeapRekursiv(heap):

    print(heap)

    heap1 = heap[:len(heap)//2] # første halvdel
    heap2 = heap[len(heap)//2:] # andre halvdel inkl.

    
    print(heapq.heappop(heap2)) # starte i andre halvdel
    heap2.sort()

    if len(heap2 ) > 1:
        FinnMidtenAvHeapRekursiv(heap2)


    if len(heap2) == 2:
        print(heap1[1])
    
    print(heapq.heappop(heap1)) # starte i andre halvdel
    heap1.sort()

    if len(heap1) > 1:
        FinnMidtenAvHeapRekursiv(heap1)


def main():

    li = []
    for _ in range(int(input())):
        heapq.heappush(li, int(input()))

def test():

    li = []
    for i in range(11):
        heapq.heappush(li, i)
    print(li)
    FinnMidtenAvHeapRekursiv(li)

test()

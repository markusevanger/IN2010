import heapq

def FinnMidtenAvHeapRekursiv(heap):

    heap1 = heap[:len(heap)//2] # forrerste
    heap2 = heap[len(heap)//2:] #bakerste

    if len(heap2) > 2:
        print(heapq.heappop(heap2))
        heap2.sort()
        FinnMidtenAvHeapRekursiv(heap2)

    elif len(heap2) > 0:
        for tall in reversed(heap2):
            print(tall)
    

    if len(heap1) > 2: 
        FinnMidtenAvHeapRekursiv(heap1)
        print(heapq.heappop(heap1))
        heap1.sort()
        

    elif len(heap1) > 0:
        for tall in reversed(heap1):
            print(tall)
    






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

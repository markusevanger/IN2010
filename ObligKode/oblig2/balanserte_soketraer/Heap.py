import heapq

def PrintSomSoketre(heap):
    
    print("--------------")

    # Må spesifisere dette fordi listene er kjeve
    if len(heap) == 2:
        print(heap[1])

    if len(heap) > 1:

        heap1 = heap[len(heap)//2:]
        heap2 = heap[:(len(heap)//2)]
        
        #print(heap1, len(heap1)," | ", heap2,len(heap1))
        print(heapq.heappop(heap1))
        heap1.sort()
        #print(heap1, len(heap1)," | ", heap2,len(heap1))
        PrintSomSoketre(heap1)

        #print(heap1, len(heap1)," | ", heap2,len(heap1))
        print(heapq.heappop(heap2))
        heap2.sort()
        #print(heap1, len(heap1)," | ", heap2,len(heap1))
        PrintSomSoketre(heap2)

    elif len(heap) == 1:
        print(heapq.heappop(heap))


def main():

    li = []
    for _ in range(int(input())):
        pass

    for i in li:
        print(i)

def test():

    li = []
    for i in range(11):
        heapq.heappush(li, i)
    print(li)
    PrintSomSoketre(li)

test()

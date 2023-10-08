import heapq


# Har kjøretid O(n(log(n)))
# Gjør log(n) steg i algoritmen, n ganger rekursivt. 

def finnMidtenNy(heap): # [0, 1, 2 ... 10]

    if len(heap) > 1:
        nyHeap = []
        for i in range(len(heap)//2):
            heapq.heappush(nyHeap, heapq.heappop(heap))
            # nyHeap = [0, 1, 2, 3, 4]
        print(heapq.heappop(heap)) # pop minste fra [5, 6, ... 10]

        # rekursivt fortsett med heap først
        finnMidtenNy(heap)
        finnMidtenNy(nyHeap) # deretter ny heap

    # om len(heap) = 1, kan vi ikke lenger splitte/iterere gjennom listen. Dermed egen if sjekk.
    elif len(heap) == 1:
        print(heapq.heappop(heap)) 



def main():

    li = []
    for _ in range(int(input())):
        heapq.heappush(li, int(input()))
    finnMidtenNy(li)
main()
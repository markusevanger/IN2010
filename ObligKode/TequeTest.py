from Teque import Teque

def main():

    tq = Teque()

    for n in range(int(input())):
        S = input().split(" ")
        x = S[1] 
        S = S[0]
        
        if S == "push_back":
            tq.push_back(x)
        if S == "push_front":
            #tq.push_front(x)
            pass
        if S == "push_middle":
            #tq.push_middle(x)
            pass
        if S == "get":
            #tq.get(x)
            pass

    print()
    n = tq.d2.head
    while n != None:
        print(n, end=", ")
        n = n.neste
    
    n = tq.d2.head
    print(" | ", end="")

    while n != None:
        print(n, end=", ")
        n = n.neste

main()
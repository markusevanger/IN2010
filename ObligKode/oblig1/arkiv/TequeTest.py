from Teque import Teque
from TequeList import TequeList

def fillTest():

    tq = Teque()
    tql = TequeList()

    for n in range(int(input())):
        S = input().split(" ")
        x = S[1] 
        S = S[0]
        
        
        if S == "push_back":
            tq.push_back(x)
            tql.push_back(x)
        if S == "push_front":
            tq.push_front(x)
            tql.push_front(x)
        if S == "push_middle":
            tq.push_middle(x)
            tql.push_middle(x)
        if S == "get":
            tq.get(x)
            tql.get(x)

    print(tq)
    print(tql.teque)

fillTest()
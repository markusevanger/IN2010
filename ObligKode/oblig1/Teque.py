
from collections import deque
from TequeList import TequeList

class Teque:

    def __init__(self):
        self.d1 = deque()
        self.d2 = deque()

    def push_front(self, x):
        self.d1.appendleft(x)

        # balansere deques om len(d1) er 1< enn len(d2)
        if len(self.d2) < len(self.d1)-1:
            self.d2.appendleft(self.d1.pop())

    def push_back(self, x):
        self.d2.append(x)

        if len(self.d1) < len(self.d2)-1:
            self.d1.append(self.d2.popleft())

    def push_middle(self, x):
        if len(self.d2) < len(self.d1)-1:
            self.d2.appendleft(self.d1.pop())
        self.d1.append(x)

    # 
    def get(self, i):

        if len(self.d1) > i:
            print(self.d1[i], end=", ")
        else:
            print(self.d2[i - len(self.d1)], end=", ")

    def hent(self, i):
        if len(self.d1) > i:
            return self.d1[i]
        else:
            return self.d2[i - len(self.d1)]

    def __str__(self):

        for i in range(len(self.d1)):
                print(self.d1[i], end=", ")

        # print("|", end=" ") # skiller lister

        for i in range(len(self.d2)):
                print(self.d2[i], end= ", ")

        return ""

def print_alle(tq, tql):
    for i in range(len(tql)):
        tall1 = tq.hent(i)
        tall2 = tql.hent(i)
        
        if tall1 != tall2:
            print(tall1, tall2)

def main():

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
            tq.get(int(x))
            tql.get(int(x))
            print()

    print_alle(tq, tql)
main()

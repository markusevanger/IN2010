
from collections import deque
import sys, time

class Teque:

    def __init__(self):
        self.d1 = deque()
        self.d2 = deque()

    def push_front(self, x):
        self.d1.appendleft(x)
        self.balance()

    def push_back(self, x):
        self.d2.append(x)
        self.balance()

    def push_middle(self, x):
        self.d2.appendleft(x)
        self.balance()

    def balance(self):
        
        differanse = len(self.d1) - len(self.d2)

        if differanse > 1:
            self.d2.appendleft(self.d1.pop())

        elif differanse <= -1:
            self.d1.append(self.d2.popleft())
            
    def __getitem__(self, i): # idk e mayby raskere?

        if len(self.d1) > i:
            return(self.d1[i])
        return(self.d2[i - len(self.d1)])

def kjor():
    tq = Teque()

    for _ in range(int(input())):
        S = sys.stdin.readline().split()
        x = S[1] # bedre om x er string, da slipper vi konkattinering, rasker
        S = S[0]
        

        if S == "push_back":
            tq.push_back(x)
        elif S == "push_front":
            tq.push_front(x)
        elif S == "push_middle":
            tq.push_middle(x)
        else:
            sys.stdout.write(tq[int(x)] + "\n")

#start_time = time.time()
kjor()
#end_time = time.time()
#print("kjor tok", end_time - start_time, "sekunder")

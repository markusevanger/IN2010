
from collections import deque
import sys, time

class Teque:

    def __init__(self):
        self.front = deque()
        self.back = deque()

    def push_front(self, x):
        self.front.appendleft(x)
        self.balance()

    def push_back(self, x):
        self.back.append(x)
        self.balance()

    def push_middle(self, x):
        self.back.appendleft(x)
        self.balance()

    # sjekker
    def balance(self):
     
        len_back = len(self.back)
        differanse = len(self.front) - len_back

        if differanse > 1:
            self.back.appendleft(self.front.pop())

        elif differanse <= -1:
            self.front.append(self.back.popleft())
            
    def __getitem__(self, i): # idk e mayby raskere?

        if len(self.front) > i:
            return(self.front[i])
        return(self.back[i - len(self.front)])

def kjor():
    tq = Teque()

    for i in range(int(input())):
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

start_time = time.time()
kjor()
end_time = time.time()
print("kjor tok", end_time - start_time, "sekunder")

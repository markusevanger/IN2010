
teque = []

def push_back(x):
    teque.append(x)
def push_front(x):
    teque.insert(0, x)
def push_middle(x):
    teque.insert((len(teque)+1) // 2, x)
def get(i):
    print(teque[int(i)])

def main():
    for n in range(int(input())):
        S = input().split(" ")
        x = S[1], S = S[0]
        
        if S == "push_back":
            push_back(x)
        if S == "push_front":
            push_front(x)
        if S == "push_middle":
            push_middle(x)
        if S == "get":
            get(x)

main()

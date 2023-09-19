


class TequeList:

    def __init__(self):
        self.teque = []

    def push_back(self, x):
        self.teque.append(x)
    def push_front(self, x):
        self.teque.insert(0, x)
    def push_middle(self, x):
        self.teque.insert((len(self.teque)+1) // 2, x)
    def get(self, i):
        print(self.teque[int(i)], end=", ")

# def main():
#     for n in range(int(input())):
#         S = input().split(" ")
#         x = S[1]
#         S = S[0]
#         
#         if S == "push_back":
#             push_back(x)
#         if S == "push_front":
#             push_front(x)
#         if S == "push_middle":
#             push_middle(x)
#         if S == "get":
#             get(x)


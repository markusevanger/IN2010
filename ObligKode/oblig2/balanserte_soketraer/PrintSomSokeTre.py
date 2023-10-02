def PrintSomSoketre(liste):
    if len(liste) > 1:
        midt = liste.pop(len(liste)//2)
        print(midt)
        PrintSomSoketre(liste[len(liste)//2:])
        PrintSomSoketre(liste[:len(liste)//2])
    elif len(liste) == 1:
        print(liste[0])

def main():

    li = []
    for _ in range(int(input())):
        li.append(int(input()))
    PrintSomSoketre(li)
    
def test():

    li = []
    for i in range(11):
        li.append(i)
    print(li)
    PrintSomSoketre(li)

test()
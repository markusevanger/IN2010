from Visualize import visualize
import random


# Fyller treet og oppdaterer tree.png live imens bruker oppgir stadig nye noder. 
def LiveTest(tre):

    print("Skriv inn ett tall du vil legge til i tree.png.")
    print("Skriv en tom enter for aa avslutte: ")

    svar = input()

    if svar != "":
        tre.root = tre.insert(None, int(svar))
        visualize(tre)

    svar = input()
    while svar != "":
        
        tre.insert(tre.root, int(svar))
        visualize(tre)
        svar = input()


# Fyller ett gitt tomt tre med ant antall noder
def FyllTilfeldig(tre, ant):

    tre.root = tre.insert(None, random.randint(1, 100))
    for i in range(ant-1): # ant -1 fordi vi legger til en root over.
        tre.insert(tre.root, random.randint(1, 100))
    visualize(tre)

def FyllKonstant(tre):

    tre.root = tre.insert(None, 50)
    r = tre.root
    
    tre.insert(r, 25)
    tre.insert(r, 75)
    tre.insert(r, 100)
    tre.insert(r, 60)
    tre.insert(r, 30)
    visualize(tre)
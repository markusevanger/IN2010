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

    for i in range(ant): # ant -1 fordi vi legger til en root over.
        tre.root = tre.insert(tre.root, random.randint(1, 1000))
    visualize(tre)

def FyllKonstant(tre):

    tre.root = tre.insert(50)
    tre.root = tre.insert(100)
    tre.root = tre.insert(75)
    tre.root = tre.insert(150)
    tre.root = tre.insert(10)
    tre.root = tre.insert(20)
    tre.root = tre.insert(15)
    tre.root = tre.insert(5)
    tre.root = tre.insert(1)
    tre.root = tre.insert(2)

    visualize(tre)
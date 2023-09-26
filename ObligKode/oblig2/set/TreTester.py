from Visualize import visualize
import random


# Fyller treet og oppdaterer tree.png live imens bruker oppgir stadig nye noder. 
def LiveTest(tre):

    print("Skriv inn ett tall du vil legge til i tree.png.")
    print("Skriv en tom enter for aa avslutte: ")

    svar = input()
    while svar != "":
        
        tre.root = tre.insert(tre.root, int(svar))
        visualize(tre)
        svar = input()


# Fyller ett gitt tomt tre med ant antall noder
def FyllTilfeldig(tre, ant):

    for i in range(ant): # ant -1 fordi vi legger til en root over.
        tre.root = tre.insert(tre.root, random.randint(1, 1000))
    visualize(tre)

def FyllKonstant(tre):

    tall_som_fylles = [50, 100, 75, 150, 10, 20, 15, 5, 1, 2, 3]

    for tall in tall_som_fylles:
        tre.root = tre.insert(tre.root, tall)

    visualize(tre)
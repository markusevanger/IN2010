

alle_tall = range(1,1001)
ferdig = False
teller = 0

while not ferdig:

    if len(alle_tall) % 2 != 0:
         tall = alle_tall[(len(alle_tall)//2)]
    else:
        tall = alle_tall[len(alle_tall)//2-1]

    if tall == 999:
        teller+=1

        if teller == 2:
            tall = 1000
   
    print(tall, flush=True)
    svar = input()

    if svar == "correct":
        ferdig = True
    elif svar == "higher":
        alle_tall = range(tall, alle_tall[-1]+1)

    elif svar == "lower":
        alle_tall = range(alle_tall[0], tall+1)

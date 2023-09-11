

tak = 1000
gulv = 1
ferdig = False

while not ferdig:
    
    tall = (tak + gulv) // 2
    print(tall, flush=True)
    svar = input()
    
    if svar == "correct":
        ferdig = True
    elif svar == "higher":
        gulv = tall
    elif svar =="lower":
        tak = tall
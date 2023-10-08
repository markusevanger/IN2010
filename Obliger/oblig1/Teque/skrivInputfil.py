
import random
f = open("input.txt", "w")
operasjoner = ["push_front", "push_middle", "push_back", "get"]
antall_linjer = 10000

f.write(f"{antall_linjer}\n")
for i in range(antall_linjer):
    r = random.randint(0, 3)
    r2 = random.randint(0, antall_linjer)
    f.write(f"{operasjoner[r]} {i} \n")

f.close()
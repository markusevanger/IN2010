

f = open("input.txt", "w")
operasjon = "push_middle"
antall_linjer = 100

f.write(f"{antall_linjer}\n")
for i in range(antall_linjer):
    f.write(f"{operasjon} {i} \n")

f.close()




f = open("six-degrees-of-imdb-ressursside-main/actors.tsv", "r",  encoding="utf-8")

a = []
b = set()
for l in f:
    l = l.split("\t")
    a.append(l[0])
    b.add(l[0])
print(len(a))
print(len(b))
print("diff:", len(a)-len(b))

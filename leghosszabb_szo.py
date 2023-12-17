lista = []
while True:
    i = input().strip()
    lista.append(i.split())
    if i[-5:] == "E-N-D":
        break
leghosszabb=""
for i in lista:
    for y in i:

        if len(y)>len(leghosszabb):
            leghosszabb=y
print(leghosszabb.lower())

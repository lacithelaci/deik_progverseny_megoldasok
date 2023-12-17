adatszam = int(input())
db = 0
lista = []
while db != adatszam:
    lista.append((input()))
    db += 1

for i in range(10):
    db = 0
    for y in lista:
        db += y.count(str(i))
    print(db, end=" ")

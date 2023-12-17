def prim(szam):
    osztok = 0
    for i in range(1, szam + 1):
        if szam % i == 0:
            osztok += 1
    return osztok == 2


def prim_osztok(szam):
    primosztok = set(i for i in range(1, szam + 1) if szam % i == 0 and prim(i))
    return primosztok


def csunya_szamok(osztok):
    halmaz = {3, 5, 2}
    return len(osztok.difference(halmaz)) == 0


lista = [1]
i = 2
while len(lista) != 1500:
    if csunya_szamok(prim_osztok(i)):
        lista.append(i)
    i += 1
print(lista[-1])

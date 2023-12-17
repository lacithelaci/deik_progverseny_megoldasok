def szamjegyosszeg(proba):
    szum = 0
    for i in proba:
        szum += int(i)
    return str(szum)


proba = input()
while str(proba) != "0":

    while len(proba) != 1:
        proba = szamjegyosszeg(proba)
    print(proba)
    proba = input()

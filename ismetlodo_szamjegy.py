def ismetlodo(szam):
    szam = str(szam)
    halamz = set()
    for i in str(szam):
        halamz.add(i)
    return len(halamz) == len(str(szam))


db = 0
bekert=input().split()
for i in range(int(bekert[0]), int(bekert[1]) + 1):
    if ismetlodo(i):
        db += 1
print(db)

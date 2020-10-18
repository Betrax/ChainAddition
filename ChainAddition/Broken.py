Dict1 = {0: 0}


def chain(Num, r=(1,)):
    x = r[0]
    l = len(r) - 1

    if x <= Num and (not x in Dict1 or l <= Dict1[x]):
        Dict1[x] = l
        for i in r:
            chain(Num, (x + i,) + r)


Num = 1000
chain(Num)

print(Num, Dict1[Num]+1)

List = list(Dict1.keys())

Index = List.index(Num)

print(List[1:Index+1])

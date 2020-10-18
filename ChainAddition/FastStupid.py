import time
start_time = time.time()


n = int(input())  # kan tot 8 cijfers snel(<1min), na 8 traag

BewijsN = (n + 1) / 2

List = []


def IsEven(n):
    return n % 2 == 0


def IsPrime(n):
    return all(n%x != 0 for x in range(3, n, 2))


def BigFactorCheck(n):
    for x in range(n):
        x += 1

        if n % (n - x) == 0:
            return n - x


while n > 1:
    if IsEven(n) == False:

        if IsPrime(n):
            List.append(n)
            n += -1  # Prim naar even

        else:  # Oneven
            List.append(n)
            BigFactor = BigFactorCheck(n)

            for x in range((n // BigFactor) - 2):
                x += 1
                List.append(n - BigFactor * x)

            n = n - BigFactor * (x + 1)  # lelijk, maar werkt

    while IsEven(n):
        List.append(n)
        n = n // 2

        if n == 1:
            List.append(n)

List.sort()
print(len(List), List)
if len(List) - 1 <= BewijsN:
    print(True, len(List) - 1, "<=", BewijsN)

print((time.time() - start_time), "secs")
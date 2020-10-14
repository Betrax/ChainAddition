n = int(input())

List1 = []


def IsEven(n):
    if n % 2 == 0:
        return True

    else:
        return False


def IsPrime(n):
    for x in range(n - 2):
        x += 2

        if n % x == 0:
            return False

    return True


def BigFactorCheck(n):
    for x in range(n):
        x += 1

        if n % (n - x) == 0:
            return n - x


while n > 1:
    if IsEven(n) == False:

        if IsPrime(n):
            List1.append(n)
            n += -1  # Prime to even number

        else:  # Odd number
            List1.append(n)
            BigFactor = BigFactorCheck(n)

            for x in range((n // BigFactor) - 2):
                x += 1
                List1.append(n - BigFactor * x)

            n = n - BigFactor * (x + 1)  # bad design

    while IsEven(n):
        List1.append(n)
        n = n // 2

        if n == 1:
            List1.append(n)


print(len(List1), List1)

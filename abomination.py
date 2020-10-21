for x in range(8127, 8128, 2): # dont laugh
    List2 = [1, 2]
    ListNum = []
    n = x
    z = x
    o = x

    while len(List2) >= 2:
        List2 = []
        for y in range(n):

            if 2 ** y > n:
                break
            a = 2 ** y
            List2.append(a)
        ListNum.append(len(List2))
        n = n - List2[-1]

    def IsEven(n):
        return n % 2 == 0

    def IsPrime(n):
        return all(n % x != 0 for x in range(3, n, 2))

    def BigFactorCheck(n):
        for x in range(n):
            x += 1

            if n % (n - x) == 0:
                return n - x

    def Print(List, BewijsN):
        List.sort()
        print(len(List), (ListNum[0] + len(ListNum) - 1), o)
        z = input()

    def Main(n, List=[]):
        BewijsN = (n + 1) / 2

        while n > 1:
            if IsEven(n) == False:

                if IsPrime(n):
                    List.append(n)
                    n += -1  # Prim naar even

                else:  # Oneven
                    List.append(n)
                    BigFactor = BigFactorCheck(n)

                    for x in range(1, (n // BigFactor) - 1):
                        List.append(n - BigFactor * x)

                    n = n - BigFactor * (x + 1)  # lelijk, maar werkt

            while IsEven(n):
                List.append(n)
                n = n // 2

                if n == 1:
                    List.append(n)
        Print(List, BewijsN)

    List = Main(z)

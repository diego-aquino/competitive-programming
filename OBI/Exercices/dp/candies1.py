m = 1000000007

def main():
    def total(x, index):
        if x < 0 or index < 0:
            return 0

        elif index == 0:
            if x <= limit[0]:
                return 1
            else:
                return 0

        elif x in calculated[index]:
            return calculated[index][x]

        else:
            totalWays = 0
            for v in range(limit[index] + 1):
                if x - v < 0: break
                totalWays += total(x - v, index - 1)

            calculated[index][x] = totalWays
            return totalWays % m

    n, k, limit = getInputs()

    calculated = []
    for i in range(n):
        calculated.append({})

    waysToShare = total(k, n - 1)
    print(waysToShare)

def getInputs():
    n, k = map(lambda x: int(x), input().split())
    limit = tuple(map(lambda x: int(x), input().split()))

    return n, k, limit

main()

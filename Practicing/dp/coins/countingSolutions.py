def main():
    total, coins = getInputs()
    n = len(coins)

    count = [0] * (total + 1)
    count[0] = 1

    previous = []
    for i in range(total + 1):
        previous.append([])

    for x in range(1, total + 1):
        for c in coins:
            if x >= c:
                count[x] += count[x - c]
                previous[x].append(x - c)

    ways = getAllWays(total, previous)

    for way in ways:
        coinSequence = getCoinSequece([total] +  way)
        print(" + ".join( map(lambda x: str(x), coinSequence) ))

    print(f"\nPossible ways: {count[total]}")

def getInputs():
    return int(input()), set(map(lambda x: int(x), input().split()))

def getAllWays(x, previous):
    def byNumberOfCoins(element):
        return len(element)

    ways = []

    newWays = []
    for prev in previous[x]:
        newWays.append([prev])

    while len(newWays) > 0:
        curr = newWays.pop()
        value = curr[-1]

        if value > 0:
            for prev in previous[value]:
                newWays.append(curr + [prev])
        else:
            ways.append(curr)

    ways.sort(key=byNumberOfCoins)
    return ways

def getCoinSequece(sequence):
    coinSequence = []

    for i in range(len(sequence) - 1):
        coinSequence.append(sequence[i] - sequence[i + 1])

    return coinSequence

main()

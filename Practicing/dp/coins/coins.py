coins = [1, 2, 5, 10, 20, 50, 100, 200]

def main():
    t = int(input())

    for i in range(t):
        print(solve())

def solve():
    x = int(input())

    return formatted(coinsToSum(x))

def coinsToSum(x):
    if x == 0:
        return [(0, 0)]

    coinsList = []
    lastCoinIndex = len(coins) - 1

    while x > 0:
        for i in range(lastCoinIndex, - 1, - 1):
            factor = x // coins[i]

            if factor > 0:
                coinsList.append((coins[i], factor))
                x -= coins[i] * factor
                lastCoinIndex = i - 1
                break

    return coinsList

def formatted(coinsList):
    if coinsList == [(0, 0)]:
        return "0"

    message = "|"

    for pair in coinsList:
        message += " {} (x{}) |".format(*pair)

    return message

main()

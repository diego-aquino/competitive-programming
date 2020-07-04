infinity = 1000000
N = 10

def getInputs():
    return int(input()), tuple(map(lambda x: int(x), input().split()))

def iterative():
    total, coins = getInputs()

    first = [0] * (total + 1)
    value = [infinity] * (total + 1)
    value[0] = 0
    for c in coins:
        value[c] = 1

    for x in range(1, total + 1):
        for c in coins:
            if (value[x - c] > 0) and (value[x - c] + 1 < value[x]):
                value[x] = value[x - c] + 1
                first[x] = c

    print("Number of coins: {}".format(value[total]))

    sequenceMsg = "Sequence: "
    while True:
        sequenceMsg += f"{first[x]}-"
        x -= first[x]

        if first[x] == 0:
            sequenceMsg += f"{x}"
            print(sequenceMsg)
            break

iterative()

def iterative2():
    from collections import deque

    infinity = 1000000

    total, coins = getInputs()

    first = [0] * (total + 1)

    valuesLeft = []

    value = [infinity] * (total + 1)
    ready = [False] * (total + 1)

    value[0] = 0
    ready[0] = True
    for c in coins:
        value[c] = 1
        ready[c] = True

    valuesLeft.append(total)

    while len(valuesLeft) > 0:
        x = valuesLeft.pop()

        newValues = deque()
        possible = False

        for c in coins:
            if x - c >= 0 and ready[x - c] != None:
                possible = True

                if ready[x - c]:
                    if value[x - c] + 1 < value[x]:
                        value[x] = value[x - c] + 1
                        ready[x] = True
                        first[x] = c
                else:
                    newValues.append(x - c)

        if possible:
            if not ready[x]:
                newValues.appendleft(x)
        else:
            ready[x] = None

        valuesLeft.extend(newValues)


    if ready[x] == None:
        print("Not possible")
    else:
        print(value[total])

        sequence = ""
        x = total
        while True:
            if first[x] == 0:
                sequence += f"{x}"
                break
            else:
                sequence += f"{first[x]}-"
                x -= first[x]

        print(sequence)

def recursive():
    def solve(value):
        if value < 0:
            return infinity

        if value in databank:
            return databank[value]
        else:
            solutions = set()
            for coin in coins:
                solutions.add(solve(value - coin) + 1)

            solution = min(solutions)

            databank[value] = solution
            return solution

    def getInputs():
        return int(input()), tuple(map(lambda x: int(x), input().split()))

    t = int(input())
    for i in range(t):
        total, coins = getInputs()

        databank = {0: 0}
        for coin in coins:
            databank[coin] = 1

        print(solve(total))

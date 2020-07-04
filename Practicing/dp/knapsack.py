def main():
    weights = getInputs()

    maxSum = sum(weights)

    uniqueWeights = set(weights)

    maxUse = {}
    for w in weights:
        if w in maxUse:
            maxUse[w] += 1
        else:
            maxUse[w] = 1

    possibleSum = [0] * (maxSum + 1)
    possibleSum[0] = 1
    possibleSum[maxSum] = 1
    for w in maxUse:
        possibleSum[w] = 1

    used = []
    for i in range(maxSum + 1):
        used.append([])

    used[0].append({0: 0})
    used[maxSum].append(maxUse)

    for w in uniqueWeights:
        used[w].append({w: 1})

    for x in range(1, maxSum + 1):
        if possibleSum[x] == 1:
            continue

        for w in uniqueWeights:
            if (x - w >= 0) and (possibleSum[x - w] == 1):
                for chain in used[x - w]:
                    if w not in chain:
                        possibleSum[x] = 1

                        newChain = chain.copy()
                        newChain[w] = 1

                        if used[x].count(newChain) == 0:
                            used[x].append(newChain)

                    elif chain[w] < maxUse[w]:
                        possibleSum[x] = 1

                        newChain = chain.copy()
                        newChain[w] += 1

                        if used[x].count(newChain) == 0:
                            used[x].append(newChain)

    print(f"\nTotal of possible sums: {sum(possibleSum)}\n")

    for value in range(maxSum + 1):
        if value == 0:
            print(f"0: 0 (x0)")

        else:
            for chain in used[value]:
                msg = f"{value}: "

                for w in uniqueWeights:
                    if w in chain:
                        msg += f"{w} (x{chain[w]}) + "

                print(msg[:-3])

def getInputs():
    return tuple(map(lambda x: int(x), input().split()))

main()

def main():
    n, maxW, weight, value = getInputs()

    accumulatedValue = [0] * (maxW + 1)
    # accumulatedValue = {0: 0}

    possible = [False] * (maxW + 1)
    possible[0] = True

    used = []
    for i in range(maxW + 1):
        used.append([0] * n)

    for x in range(min(weight), maxW + 1):
        for w in range(n):
            weightW = weight[w]

            if (x - weightW >= 0) and possible[x - weightW] and used[x - weightW][w] == 0:
                newValue = accumulatedValue[x - weightW] + value[w]

                if newValue > accumulatedValue[x]:
                    accumulatedValue[x] = newValue
                    used[x] = used[x - weightW].copy()
                    used[x][w] = 1
                    possible[x] = True

    print(max(accumulatedValue))

def getInputs():
    n, maxW = map(lambda x: int(x), input().split())

    weight, value = [], []
    for i in range(n):
        w, v = map(lambda x: int(x), input().split())
        weight.append(w)
        value.append(v)

    return n, maxW, weight, value

main()

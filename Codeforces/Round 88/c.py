def main():
    t = int(input())

    for case in getCases(t):
        print(minCups(case))

def getCases(t):
    cases = []
    for i in range(t):
        cases.append(list(map(lambda x: int(x), input().split())))

    return cases

def minCups(case):
    hotSource, coldSource, desiredTemp = case

    totalTemp = 0
    cups = 0

    high = [hotSource, 1]
    low = [(hotSource + coldSource) / 2, 2]

    while True:
        cups += 1
        if cups % 2 == 1:
            totalTemp += hotSource
        else:
            totalTemp += coldSource

        currTemp = totalTemp / cups

        if currTemp > desiredTemp:
            if currTemp < high[0]:
                high[0] = currTemp
                high[1] = cups
        elif currTemp < desiredTemp:
            if cups % 2 == 1:
                if currTemp > low[0]:
                    low[0] = currTemp
                    low[1] = cups
                else:
                    if abs(desiredTemp - high[0]) < abs(desiredTemp - low[0]):
                        return high[1]
                    else:
                        return low[1]
        else:
            return cups

main()

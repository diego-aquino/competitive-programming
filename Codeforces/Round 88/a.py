def main():
    t = int(input())

    for case in getCases(t):
        print(maxPoints(case))

def getCases(t):
    cases = []
    for i in range(t):
        cases.append(input().split())

    return cases

def maxPoints(case):
    for i in range(3):
        case[i] = int(case[i])

    cardsPerPLayer = case[0] // case[2]

    jokers = case[1]

    k = case[2]
    players = [0] * k

    if jokers <= cardsPerPLayer:
        players[0] = jokers
        jokers = 0
    else:
        players[0] = cardsPerPLayer
        jokers -= cardsPerPLayer


    jokersPerLoser = jokers / (k - 1)

    if jokersPerLoser == int(jokersPerLoser):
        for j in range(1, k):
            players[j] = int(jokersPerLoser)

    else:
        jokersPerLoser = int(jokersPerLoser)

        if jokersPerLoser == 0:
            for j in range(1, k - 1):
                if jokers <= 0: break

                players[j] = 1
                jokers -= 1
        else:
            for j in range(1, k - 1):
                if jokers <= 0: break

                players[j] = jokersPerLoser
                jokers -= jokersPerLoser

        players[-1] = jokers

    if players[0] == players[-1]:
        return 0
    else:
        return players[0] - max(players[1:])

main()

from collections import deque

infinity = 200

def main():
    n, ins, age, ger = getInputs()

    for i in range(ins):
        action = input().split()

        if action[0] == "T":
            a, b = map(lambda x: int(x) - 1, action[1:])

            for j in range(n):
                if (a not in ger[j]) or (b not in ger[j]):
                    if a in ger[j]:
                        ger[j].remove(a)
                        ger[j].add(b)
                    elif b in ger[j]:
                        ger[j].remove(b)
                        ger[j].add(a)

            ger[a], ger[b] = ger[b], ger[a]

        else:
            e = int(action[1]) - 1

            if len(ger[e]) > 0:
                youngest = infinity

                visited = set()
                toVisit = deque([e])

                while len(toVisit) > 0:
                    for boss in ger[toVisit[0]]:
                        if age[boss] < youngest:
                            youngest = age[boss]

                        if boss not in visited:
                            toVisit.append(boss)

                    visited.add(toVisit.popleft())

                print(youngest)
            else:
                print("*")

def getInputs():
    n, m, ins = map(lambda x: int(x), input().split())
    age = list(map(lambda x: int(x), input().split()))

    ger = []
    for i in range(n):
        ger.append(set())

    for i in range(m):
        x, y = map(lambda x: int(x) - 1, input().split())
        ger[y].add(x)

    return n, ins, age, ger

main()

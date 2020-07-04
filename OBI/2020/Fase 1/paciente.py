def main():
    n, c = map(lambda x: int(x), input().split())

    infectedLeft = set(range(1, n + 1))
    for i in range(c):
        infectedChain = set(map(lambda x: int(x), input().split()[2:]))

        for infected in infectedChain:
            infectedLeft.remove(infected)

    zeros = list(infectedLeft)
    zeros.sort()

    for p in zeros:
        print(p)

main()

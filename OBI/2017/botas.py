def main():
    n = int(input())

    pairs = 0

    boots = {}

    for i in range(n):
        boot = input().split()

        if boot[0] in boots:
            if boot[1] == "D":
                counterSide = "E"
            else:
                counterSide = "D"

            if boots[boot[0]][counterSide] > 0:
                boots[boot[0]][counterSide] -= 1
                pairs += 1
            else:
                boots[boot[0]][boot[1]] += 1
        else:
            boots[boot[0]] = {"E": 0, "D": 0}
            boots[boot[0]][boot[1]] = 1

    print(pairs)

main()

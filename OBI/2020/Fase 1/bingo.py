def main():
    n = int(input().split()[0])

    card = []
    for i in range(n):
        card.append(
            set(map(lambda x: int(x), input().split()))
        )

    luckNums = tuple(map(lambda x: int(x), input().split()))

    winners = []

    for num in luckNums:
        for i in range(n):
            if num in card[i]:
                card[i].remove(num)

                if len(card[i]) == 0:
                    winners.append(i + 1)

        if len(winners) > 0:
            break

    winners.sort()
    print(" ".join(map(lambda x: str(x), winners)))

main()

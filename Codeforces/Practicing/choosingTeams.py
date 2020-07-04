def main():
    n, k = map(lambda x: int(x), input().split())
    participations = list(map(lambda x: int(x), input().split()))

    validParticipants = 0
    for part in participations:
        if part + k <= 5:
            validParticipants += 1

    print(validParticipants // 3)

main()

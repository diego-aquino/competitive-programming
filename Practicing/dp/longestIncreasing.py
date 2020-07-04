def main():
    sequence = list(map(lambda x: int(x), input().split()))
    n = len(sequence)

    length = [0] * n
    previous = [None] * n

    length[0] = 1

    for i in range(1, n):
        longestLength = 0
        prev = None

        for j in range(i):
            if sequence[j] < sequence[i] and length[j] > longestLength:
                longestLength = length[j]
                prev = j

        length[i] = longestLength + 1
        previous[i] = prev

    msg = ""

    maxLength = 0
    for i in range(n):
        if length[i] > maxLength:
            maxLength = length[i]
            curr = i

    print(maxLength)

    while True:
        msg = f"{sequence[curr]} - {msg}"

        curr = previous[curr]
        if curr == None: break

    print(msg[:-3])

main()

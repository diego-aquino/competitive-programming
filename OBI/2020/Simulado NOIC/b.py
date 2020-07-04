def main():
    n, h = getInputs()

    longest = 1

    i = 0
    while i < n:
        length = 1
        for j in range(i + 1, n):
            if h[j] > h[i]:
                length += 1
                i += 1
            else: break

        if length > longest:
            longest = length

        i += 1

    print(longest)

def getInputs():
    return int(input()), list(map(lambda x: int(x), input().split()))

main()

def main():
    s, t = input(), input()
    if len(s) > len(t):
        s, t = t, s

    n, m = len(s), len(t)

    length = [0] * n
    limit = [0] * n
    previous = [None] * n

    if t.count(s[0]) > 0:
        length[0] = 1
        limit[0] = t.index(s[0])

    for i in range(1, n): # for each char in s
        for j in range(i - 1, -1, -1): # for each char at the left of s[i]
            if length[j] + 1 > length[i]:
                for k in range(limit[j], m): # find the current char to the right of the limit of the sequence
                    if t[k] == s[i]:
                        length[i] = length[j] + 1
                        limit[i] = k + 1
                        previous[i] = j
                        break

        if limit[i] == 0:
            limit[i] = m

    print(length)
    print(limit)
    print(previous)

    longestLength = -1
    for k in range(n):
        if length[k] > longestLength:
            longestLength = length[k]
            curr = k

    subsequence = ''

    if longestLength > 0:
        while True:
            subsequence = f'{s[curr]}{subsequence}'

            curr = previous[curr]
            if curr == None: break

    print(subsequence)

main()

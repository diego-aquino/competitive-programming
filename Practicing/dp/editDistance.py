def main():
    s1, s2 = getInputs()
    n, m = len(s1), len(s2)

    distance = []
    for i in range(n + 1):
        distance.append([0] * (m + 1))

    for row in range(n + 1):
        distance[row][0] = row
    for column in range(m + 1):
        distance[0][column] = column

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]
            else:
                distance[i][j] = 1 + min(
                    distance[  i  ][j - 1],
                    # eliminating the last element from s1 and comparing the
                    # distance to turn the remaining substring from s1 into the
                    # current substring from s2 ...

                    distance[i - 1][  j  ],
                    # eliminating the last element from s2 and comparing the
                    # distance to turn the remaining substring from s2 into the
                    # current substring from s1 ...

                    distance[i - 1][j - 1],
                    # eliminating the last element from both s1 and s2 and
                    # comparing the distance to turn the remaining substrings
                    # into each other ...

                    # ... then adding the new character at the end of the
                    # substring (1 + ...)
                )

    def byValue(point):
        return distance[point[0]][point[1]]

    points = []
    curr = (n, m)

    while True:
        points.append(curr)
        if curr == (0, 0): break

        if s1[curr[0] - 1] == s2[curr[1] - 1]:
            curr = (curr[0] - 1, curr[1] - 1)
        else:
            adjacent = [
                (curr[0], curr[1] - 1),
                (curr[0] - 1, curr[1]),
                (curr[0] - 1, curr[1] - 1),
            ]
            adjacent.sort(key=byValue)

            curr = adjacent[0]

    points.reverse()

    print(distance[-1][-1])
    print(points)

def getInputs():
    s1, s2 = input(), input()
    return min(s1, s2), max(s1, s2)

main()

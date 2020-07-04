from collections import deque

def main():
    n, f = map(lambda x: int(x), input().split())

    area = []
    for i in range(n):
        inputData = input()

        line = []
        for char in inputData:
            line.append(char)

        area.append(line)

    if int(area[0][0]) <= f:
        toVisit = deque([(0, 0)])
        area[0][0] =  "*"

        while len(toVisit) > 0:
            curr = toVisit.popleft()

            for delta in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                point = (curr[0] + delta[0], curr[1] + delta[1])

                if (0 <= point[0] < n) and (0 <= point[1] < n):
                    char = area[point[0]][point[1]]

                    if char != "*" and int(char) <= f:
                        area[point[0]][point[1]] =  "*"
                        toVisit.append(point)

    for row in area:
        print("".join(row))

main()

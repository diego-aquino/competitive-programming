from collections import deque

def main():
    onesLeft = getInputs()

    if len(onesLeft) > 0:
        sizes = []

        toVisit = deque([onesLeft.pop()])
        currSize = 1

        while True:
            curr = toVisit.popleft()

            for deltaX in [-1, 1]:
                point = (curr[0], curr[1] + deltaX)

                if point in onesLeft:
                    toVisit.append(point)
                    onesLeft.remove(point)
                    currSize += 1

            for deltaY in [-1, 1]:
                point = (curr[0] + deltaY, curr[1])

                if point in onesLeft:
                    toVisit.append(point)
                    onesLeft.remove(point)
                    currSize += 1

            if len(toVisit) == 0:
                sizes.append(currSize)

                if len(onesLeft) > 0:
                    currSize = 1
                    toVisit.append(onesLeft.pop())
                else: break

        print(sizes)

    else:
        print(0)

def getInputs():
    n, m = map(lambda x: int(x), input().split())

    matrix = []
    for i in range(n):
        matrix.append(list(map(lambda x: int(x), input().split())))

    onesLeft = set()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                onesLeft.add((i, j))

    return onesLeft

main()

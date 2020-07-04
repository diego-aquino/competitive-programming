def main():
    n, factor = getInputs()

    points = []
    for i in range(n):
        points.append([0] * 3)

    # points[day][pile]
    for pile in range(3):
        points[0][pile] = factor[0][pile]

    for day in range(1, n):
        points[day][0] = max(points[day - 1][1], points[day - 1][2]) + factor[day][0]
        points[day][1] = max(points[day - 1][0], points[day - 1][2]) + factor[day][1]
        points[day][2] = max(points[day - 1][0], points[day - 1][1]) + factor[day][2]

    print(max(points[-1]))

def getInputs():
    n = int(input())

    factor = []
    for i in range(n):
        factor.append(tuple(map(lambda x: int(x), input().split())))

    return n, factor

main()

def main():
    points = []
    for i in range(2):
        data = input().split()

        points.extend([
            list(map(lambda x: int(x), data[:2])),
            list(map(lambda x: int(x), data[2:]))
        ])

    areas = [
        abs(points[0][0] - points[1][0]) * abs(points[0][1] - points[1][1]),
        abs(points[2][0] - points[3][0]) * abs(points[2][1] - points[3][1])
    ]

    total = 0

    minX1 = min(points[0][0], points[1][0])
    maxX1 = max(points[0][0], points[1][0])
    minY1 = min(points[0][1], points[1][1])
    maxY1 = max(points[0][1], points[1][1])

    minX2 = min(points[2][0], points[3][0])
    maxX2 = max(points[2][0], points[3][0])
    minY2 = min(points[2][1], points[3][1])
    maxY2 = max(points[2][1], points[3][1])

    if areas[0] < areas[1]:
        for i in range(minX1, maxX1):
            if minX2 <= i < maxX2:
                for j in range(minY1, maxY1):
                    if minY2 <= j < maxY2:
                        total += 1
    else:
        for i in range(minX2, maxX2):
            if minX1 <= i < maxX1:
                for j in range(minY2, maxY2):
                    if minY1 <= j < maxY1:
                        total += 1

    print(total)

main()

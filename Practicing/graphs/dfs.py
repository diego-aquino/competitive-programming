matriz = [
    [1, 2, 3],
    [0, 2],
    [0, 1, 4],
    [0],
    [2]
]

for i in range(len(matriz)):
    total = 0

    visited = set([])
    toVisit = [i]

    while len(toVisit) > 0:
        start = toVisit.pop()
        for dest in matriz[start]:
            if dest not in visited:
                toVisit.append(dest)
                total += 1

        visited.add(start)

    print(total)

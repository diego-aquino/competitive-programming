from collections import deque

def main():
    n, adj = getInputs()

    # maxDistance[start]
    maxDistance = [0] * n
    overallMaxDistance = 0

    calculated = [0] * n

    for v in getVertexSequence(n, adj):
        # distance[dest] (starting at v)
        distance = [0] * n
        currMaxDistance = 0

        toVisit = deque([v])

        while len(toVisit) > 0:
            curr = toVisit.popleft()

            for dest in adj[curr]:
                if calculated[dest] == 1:
                    newDistance = distance[curr] + maxDistance[dest] + 1

                    if newDistance > distance[dest]:
                        distance[dest] = newDistance

                        if distance[dest] > currMaxDistance:
                            currMaxDistance = distance[dest]
                else:
                    if distance[curr] + 1 > distance[dest]:
                        distance[dest] = distance[curr] + 1

                        if distance[dest] > currMaxDistance:
                            currMaxDistance = distance[dest]

                    toVisit.append(dest)

        maxDistance[v] = currMaxDistance
        if currMaxDistance > overallMaxDistance:
            overallMaxDistance = currMaxDistance

        calculated[v] = 1

    print(overallMaxDistance)

def getInputs():
    n, m = map(lambda x: int(x), input().split())

    adj = []
    for i in range(n):
        adj.append([])

    for i in range(m):
        a, b = map(lambda x: int(x), input().split())
        adj[a - 1].append(b - 1)

    return n, adj

def getVertexSequence(n, adj):
    pairs = []
    for i in range(n):
        pairs.append((i, adj[i]))

    pairs.sort(key=(lambda x: len(x[1])))

    sequence = []
    for i in range(n):
        sequence.append(pairs[i][0])

    return sequence

main()

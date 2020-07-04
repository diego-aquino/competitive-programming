def main():
    n, adj = getInputs()
    start = 3
    print(farthestDistanceFrom(start, n, adj))

def farthestDistanceFrom(start, n, adj):
    distances = [-1] * n
    distances[start] = 0
    previous = [None] * n

    visited = set()
    unvisited = set(range(n))

    while len(unvisited) > 0:
        curr = getFarthestNode(unvisited, distances)
        unvisited.remove(curr)
        visited.add(curr)

        for dest in unvisited:
            edge = adj[curr][dest]

            if edge > 0:
                distance = distances[curr] + edge

                if distance > distances[dest]:
                    distances[dest] = distance
                    previous[dest] = curr

    farthestDistance = 0
    for i in range(n):
        if distances[i] > farthestDistance:
            farthestDistance = distances[i]
            farthestNode = i

    return farthestNode, farthestDistance

def getFarthestNode(unvisited, distances):
    farthestDistance = -1

    for node in unvisited:
        if distances[node] > farthestDistance:
            farthestDistance = distances[node]
            farthestNode = node

    return farthestNode

def getInputs():
    n, m = map(lambda x: int(x), input().split())

    adj = []
    for i in range(n):
        adj.append([0] * n)

    for i in range(m):
        a, b, weight = map(lambda x: int(x), input().split())
        adj[a][b] = weight
        adj[b][a] = weight

    return n, adj

main()

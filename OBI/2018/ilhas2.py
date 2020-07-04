infinity = 10000000000

def main():
    n, s, adj = getInputs()

    distancesFromS = dij(n, s, adj)
    print(max(distancesFromS) - min(distancesFromS))

def dij(n, start, adj):
    distances = [infinity] * n
    distances[start] = 0
    previous = [None] * n

    visited = set()
    unvisited = set(range(n))

    while len(unvisited) > 0:
        curr = closestNode(unvisited, distances)
        unvisited.remove(curr)
        visited.add(curr)

        for dest in unvisited:
            edge = adj[curr][dest]

            if edge > 0:
                distance = distances[curr] + edge

                if distance < distances[dest]:
                    distances[dest] = distance
                    previous[dest] = curr

    return distances[:start] + distances[start + 1:]

def closestNode(unvisited, distances):
    shortestEdge = infinity

    for node in unvisited:
        if distances[node] < shortestEdge:
            shortestEdge = distances[node]
            closestNode = node

    return closestNode

def getInputs():
    n, m = map(lambda x: int(x), input().split())

    adj = []
    for i in range(n):
        adj.append([0] * n)

    for i in range(m):
        a, b, weight = map(lambda x: int(x), input().split())
        adj[a - 1][b - 1] = weight
        adj[b - 1][a - 1] = weight

    s = int(input()) - 1

    return n, s, adj

main()

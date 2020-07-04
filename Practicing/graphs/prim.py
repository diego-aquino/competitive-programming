infinity = 1000000

def main():
    n, adj = getInputs()

    totalDistance = prim(n, adj)
    print(totalDistance)

def getInputs():
    n, m = map(lambda x: int(x), input().split())

    adj = []
    for i in range(n):
        adj.append([0] * n)

    for i in range(m):
        a, b, weight = map(lambda x: int(x), input().split())
        adj[a - 1][b - 1] = weight
        adj[b - 1][a - 1] = weight

    return n, adj

def prim(n, adj):
    totalDistance = 0

    visited = set()
    unvisited = set(range(n))

    curr = 0
    while len(unvisited) > 1:
        unvisited.remove(curr)
        visited.add(curr)

        dest, edge = getClosestNode(curr, unvisited, adj)

        totalDistance += edge
        curr = dest

    return totalDistance

def getClosestNode(curr, unvisited, adj):
    shortestEdge = infinity

    for node in unvisited:
        edge = adj[curr][node]
        if 0 < edge < shortestEdge:
            shortestEdge = edge
            closestNode = node

    return closestNode, shortestEdge

main()

# 6 8
# 1 2 4
# 1 3 4
# 2 3 2
# 3 4 3
# 3 5 4
# 3 6 2
# 4 5 3
# 5 6 3

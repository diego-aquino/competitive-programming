infinity = 1000000

def main():
    n, adj = getInputs()

    start = 0
    end = 2
    distances, previous = dij(n, start, adj)

    print(path(end, previous))
    print(distances[end])

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

    return distances, previous

def closestNode(unvisited, distances):
    shortestEdge = infinity
    for node in unvisited:
        if distances[node] < shortestEdge:
            shortestEdge = distances[node]
            closestNode = node

    return closestNode

def path(end, previous):
    path = ""
    curr = end

    while True:
        path = f"{curr}-{path}"

        curr = previous[curr]
        if curr == None: break

    return path[:-1]

main()

# 5 7
# 1 2 6
# 1 4 1
# 2 4 2
# 2 5 2
# 2 3 5
# 3 5 5
# 4 5 1

# 5 6
# 1 2 1
# 1 5 3
# 2 3 1
# 3 5 1
# 3 4 2
# 4 5 1

def main():
    n, adj = getAdj()
    print(adj)
    print(isConnected(adj, n))

def isConnected(adj, n):
    visited = [0] * n
    toVisit = [0]

    while len(toVisit) > 0:
        curr = toVisit.pop()
        visited[curr] = 1

        for dest in adj[curr]:
            if not visited[dest]:
                toVisit.append(dest)

    return sum(visited) == n

def getAdj():
    n, m = map(lambda x: int(x), input().split())

    adj = []
    for i in range(n):
        adj.append([])

    for i in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        # undirected graph
        adj[a].append(b)
        adj[b].append(a)

    return n, adj

main()

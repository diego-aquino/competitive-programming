def main():
    n, adj = getInputs()
    sequence = getTopologicalSort(n, adj)

    distance = [-1] * n
    longest = -1

    for v in sequence:
        if len(adj[v]) == 0:
            distance[v] = 0
        else:
            for dest in adj[v]:
                distance[v] = max(distance[v], 1 + distance[dest])
                longest = max(longest, distance[v])

    print(longest)

def getTopologicalSort(n, adj):
    state = [0] * n
    toVisit = list(range(n))

    topologicalSort = []
    order = []

    while len(toVisit) > 0:
        curr = toVisit.pop()

        if state[curr] == 0:
            order.append(curr)
            state[curr] = 1

            foundNewDest = False
            for dest in adj[curr]:
                if state[dest] == 0:
                    toVisit.append(dest)
                    foundNewDest = True

            if not foundNewDest:
                while True:
                    v = order[-1]

                    allProcessed = True
                    for dest in adj[v]:
                        if state[dest] == 0:
                            allProcessed = False
                            break

                    if allProcessed:
                        state[v] = 2
                        topologicalSort.append(order.pop())

                    if len(order) == 0 or not allProcessed:
                        break

    return topologicalSort

def getInputs():
    n, m = map(lambda x: int(x), input().split())

    adj = []
    for i in range(n):
        adj.append([])

    for i in range(m):
        a, b = map(lambda x: int(x), input().split())
        adj[a - 1].append(b - 1)

    return n, adj

main()

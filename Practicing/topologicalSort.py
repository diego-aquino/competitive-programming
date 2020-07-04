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

def main():
    n, adj = getAdj()
    print(hasCycle(adj, n))

def hasCycle(adj, n):
    """Description:
        using dfs, store the current path from the starting node
        when there are no more available children, update the path:
            remove the last node

            check if all children of its previous node were visited:
                yes? remove it too and continue the loop
                no? stop removing nodes and proceed with the dfs until all nodes
                    have been visited

        if the dfs finds any new node that is already in the current path, a cycle
        has been found!
    """
    visited = [0] * n
    toVisit = [0]

    nodesInCurrPath = set()
    orderOfCurrPath = []

    while len(toVisit) > 0:
        curr = toVisit.pop()
        visited[curr] = 1

        foundUnvisitedChildren = False
        for dest in adj[curr]:
            if len(orderOfCurrPath) > 0 and dest == orderOfCurrPath[-1]:
                continue

            if dest in nodesInCurrPath:
                return True # loop!

            if not visited[dest]:
                toVisit.append(dest)
                foundUnvisitedChildren = True

        if foundUnvisitedChildren:
            nodesInCurrPath.add(curr)
            orderOfCurrPath.append(curr)
        else:
            while len(orderOfCurrPath) > 0:
                last = orderOfCurrPath[-1]

                allVisitedChildren = True
                for dest in adj[last]:
                    if not visited[dest]:
                        allVisitedChildren = False
                        break

                if allVisitedChildren:
                    nodesInCurrPath.remove(last)
                    orderOfCurrPath.pop()
                else:
                    break

    return False # no loop!

def getAdj():
    n, m = map(lambda x: int(x), input().split())

    adj = []
    for i in range(n):
        adj.append([])

    for i in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        # directed graph
        adj[a].append(b)
        adj[b].append(a)

    return n, adj

main()

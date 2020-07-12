from collections import deque

def main():
    n, adj = getAdj()
    print(isBipartite(adj, n))

def isBipartite(adj, n):
    """Description
        create bfs
        in each cycle, get all of the children and check if any of them are connected
        to each other
            yes? not bipartite!
            no? go for another cycle

            until all nodes have been visited

        keeping track of a cycle:
            numOfParents = 1
            numOfChildren = 0

            while numOfParents > 0: each children find means numOfChildren++
            when numOfParents == 0:
                numOfParents = numOfChildren
                numOfChildren = 0
    """
    visited = [0] * n

    toVisit = deque([0])
    visited[0] = 1

    numOfParents = 1
    childrenFound = set()

    while len(toVisit) > 0:
        curr = toVisit.popleft()

        numOfParents -= 1

        for dest in adj[curr]:
            if not visited[dest]:
                for childDest in adj[dest]:
                    if childDest in childrenFound:
                        return False

                toVisit.append(dest)
                childrenFound.add(dest)
                visited[dest] = 1

        if numOfParents == 0:
            numOfParents = len(childrenFound)
            childrenFound.clear()

    return True

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

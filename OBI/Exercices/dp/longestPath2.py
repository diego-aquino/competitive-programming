from collections import deque

def main():
    n, adj, sequence = getInputs()

    maxDistance = 0
    distance = [-1] * n

    toVisit = deque(sequence)

    while len(toVisit) > 0:
        curr = toVisit.popleft()

        if len(adj[curr]) == 0:
            distance[curr] = 0
        else:
            for dest in adj[curr]:
                if distance[dest] >= 0:
                    if (1 + distance[dest]) > distance[curr]:
                        distance[curr] = 1 + distance[dest]

                        if distance[curr] > maxDistance:
                            maxDistance = distance[curr]
                else:
                    toVisit.append(curr)
                    break

    print(maxDistance)

def getInputs():
    n, m = map(lambda x: int(x), input().split())

    adj = []
    for i in range(n):
        adj.append([])

    for i in range(m):
        a, b = map(lambda x: int(x), input().split())
        adj[a - 1].append(b - 1)

    sequence = []
    visited = [False] * n

    for v in range(n):
        if not visited[v]:
            currSequence = []
            toVisit = [v]

            while len(toVisit) > 0:
                curr = toVisit.pop()

                for dest in adj[curr]:
                    if not visited[dest]:
                        toVisit.append(dest)

                currSequence.append(curr)
                visited[curr] = True

            currSequence.reverse()
            sequence.extend(currSequence)

    return n, adj, sequence

main()

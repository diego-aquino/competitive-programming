def main():
    n, adj = getInputs()

    print('DFS:')
    dfs(n, adj)

    print('\nBFS:')
    bfs(n, adj)

def bfs(n, adj):
    from collections import deque

    start = 0

    visited = [0] * n
    visited[start] = 1

    distance = [0] * n

    toVisit = deque([start])

    while len(toVisit) > 0:
        curr = toVisit.popleft()

        print(f'> current node: {curr + 1}')

        for dest in adj[curr]:
            if not visited[dest]:
                distance[dest] = curr + 1
                visited[dest] = 1

                toVisit.append(dest)

    print('BFS complete!')
    print(distance)

def dfs(n, adj):
    visited = [0] * n
    toVisit = [0]

    while len(toVisit) > 0:
        curr = toVisit.pop()
        visited[curr] = 1

        print(f'> Visiting {curr + 1}...')

        for dest in adj[curr]:
            if not visited[dest]:
                toVisit.append(dest)

    print('DFS complete!')

def getInputs():
    n, m = map(lambda x: int(x), input().split())

    adj = []
    for i in range(n):
        adj.append([])

    for i in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        adj[a].append(b)

    return n, adj

main()

from collections import deque

def main():
    adj = [
        [1, 2, 3],
        [0, 2],
        [0, 1, 4],
        [0],
        [2]
    ]

    for i in range(len(adj)):
        start = i

        totalPaths = 0

        visited = set()
        toVisit = deque([start])

        while len(toVisit) > 0:
            for dest in adj[toVisit[0]]:
                if dest not in visited:
                    toVisit.append(dest)
                    totalPaths += 1

            visited.add(toVisit.popleft())

        print(totalPaths)

main()

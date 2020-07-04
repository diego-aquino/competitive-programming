def main():
    tasks = getTasks()
    print(optimalOrder(tasks))

def getTasks():
    n = int(input())

    tasks = []
    for i in range(n):
        duration, deadline = list(map(lambda x: int(x), input().split()))
        tasks.append((i + 1, duration, deadline))

    return tasks

def optimalOrder(tasks):
    tasks.sort(key=byDeadline)
    tasks.sort(key=byDuration)

    return getOrder(tasks)

def byDeadline(x):
    return x[2]

def byDuration(x):
    return x[1]

def getOrder(tasks):
    order = []
    for task in tasks:
        order.append(task[0])

    return order

main()

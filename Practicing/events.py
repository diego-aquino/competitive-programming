def main():
    t = int(input())
    for i in range(t):
        print(solve())

def solve():
    n = int(input())
    events = getEvents(n)

    return getEventsToAttend(events)

def getEvents(n):
    events = []
    for i in range(n):
        events.append((
            i + 1,
            *list(map(lambda x: float(x), input().split()))
        ))

    return events

def getEventsToAttend(events):
    def byEnd(x):
        return x[2]

    eventsToAttend = ""

    events.sort(key=byEnd)

    currEvent = events.pop(0)
    eventsToAttend += str(currEvent[0]) + " "
    start = currEvent[2]

    while True:
        eventFound = False

        for i in range(len(events)):
            if events[i][1] >= start:
                currEvent = events.pop(i)
                eventsToAttend += str(currEvent[0]) + " "
                start = currEvent[2]

                eventFound = True
                break

        if not eventFound:
            return eventsToAttend[:-1]

main()

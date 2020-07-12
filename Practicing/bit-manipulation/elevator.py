def main():
    """Description:
        # iterate over all subsets of the people left
            # if the total weight in the elevator is lower of equal to the max weight:
            # save the total weight for that subset

        # after iterating, find the subset with the highest valid weight

        # mark the people who belong to that subset, so that they are not counted
        # more than once

        # repeat until no more person is left
    """
    def getIdealPeopleForCurrentTrip():
        idealSubset = 0
        maxSubsetWeight = 0

        for subset in range(1, 1 << n):
            subsetWeight = 0

            for person in range(n):
                if personInSubset(person, subset) and not transported[person]:
                    if subsetWeight + weight[person] > maxWeightPerTrip:
                        break

                    subsetWeight += weight[person]

            if subsetWeight > maxSubsetWeight:
                maxSubsetWeight = subsetWeight
                idealSubset = subset

                if maxSubsetWeight == maxWeightPerTrip:
                    break

        return idealSubset

    def printPeopleIn(subset):
        peopleMsg = '> People: '
        weightMsg = '> Weights: '

        for person in range(n):
            if personInSubset(person, subset):
                peopleMsg += f'{person} '
                weightMsg += f'{weight[person]} '

        print(peopleMsg[:-1])
        print(weightMsg[:-1], end='\n\n')

    n, maxWeightPerTrip, weight = getInputs()

    transported = [False] * n
    numOfTransported = 0
    numOfTrips = 0

    while numOfTransported < n:
        idealSubset = getIdealPeopleForCurrentTrip()

        if idealSubset == 0:
            print('Not possible')
            return

        for person in range(n):
            if personInSubset(person, idealSubset):
                transported[person] = True
                numOfTransported += 1

        printPeopleIn(idealSubset)

        numOfTrips += 1

    print(numOfTrips)

def getInputs():
    n, maxWeightPerTrip = map(lambda x: int(x), input().split())
    weight = tuple(map(lambda x: int(x), input().split()))

    return n, maxWeightPerTrip, weight

def personInSubset(person, subset):
    return subset & (1 << person)

main()

# 5 10
# 2 3 3 5 6

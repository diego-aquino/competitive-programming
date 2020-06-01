def createAllSubgroups(array):
    subgroups = []

    length = 1
    while length < len(array):
        for i in range(len(array)):
            if i + length < len(array):
                subgroups.append(array[i:i+length])
            else: break

        length += 1

    return subgroups

list1 = list(range(5))

print(list1)

for group in createAllSubgroups(list1):
    print(group)

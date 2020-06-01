def main():
    stamped, got = getInputs()
    print(stampedLeft(stamped, got))

def getInputs():
    input()
    stamped = input().split()
    got = input().split()

    return stamped, got

def stampedLeft(stamped, got):
    got = sort(got)

    stampedLeft = len(stamped)

    for card in stamped:
        if found(card, got):
            stampedLeft -= 1

    return stampedLeft

def sort(array):
    n = len(array)

    if n < 2:
        return array
    elif n == 2:
        if int(array[0]) > int(array[1]):
            array[0], array[1] = array[1], array[0]
        return array
    else:
        return merge(sort(array[:n//2]), sort(array[n//2:]))

def merge(array1, array2):
    mergedList = []

    while len(array1) > 0 and len(array2) > 0:
        if int(array1[0]) < int(array2[0]):
            mergedList.append(array1.pop(0))
        else:
            mergedList.append(array2.pop(0))

    mergedList.extend(array1)
    mergedList.extend(array2)

    return mergedList

def found(element, array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (high + low) // 2

        if int(element) > int(array[mid]):
            low = mid + 1
        elif int(element) < int(array[mid]):
            high = mid - 1
        else:
            return True

    return False

main()

def main():
    stamped, got = getInputs()
    print(stampedLeft(stamped, got))

def getInputs():
    input()
    stamped = input().split()
    got = input().split()

    return stamped, got

def stampedLeft(stamped, got):
    got.sort()

    stampedLeft = len(stamped)

    for card in stamped:
        if found(card, got):
            stampedLeft -= 1

    return stampedLeft

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

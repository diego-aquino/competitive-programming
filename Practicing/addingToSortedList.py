def add(element, array):
    """Adds an element to a sorted array, so that it remains sorted."""

    properIndex = find(element, array)

    if element > array[properIndex]:
        array.insert(properIndex + 1, element)
    else:
        array.insert(properIndex, element)


def find(element, array):
    """Returns the index of an element in an sorted array by using binary search.
    If the element is not found, returns the closest index where it should be."""

    bottom = 0
    top = len(array) - 1

    while bottom <= top:
        middle = (top + bottom) // 2

        if element < array[middle]:
            top = middle - 1
        elif element > array[middle]:
            bottom = middle + 1
        else:
            return middle

    return middle


array = [1, 2, 3, 8, 9, 11, 17]
add(14, array)

print(array)

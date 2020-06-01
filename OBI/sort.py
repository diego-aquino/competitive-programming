def sort(sequence):
    n = len(sequence)

    if n < 2:
        return sequence
    elif n == 2:
        if sequence[0] > sequence[1]:
            sequence[0], sequence[1] = sequence[1], sequence[0]
        return sequence
    else:
        return merge(sort(sequence[:n//2]), sort(sequence[n//2:]))

def merge(sequence1, sequence2):
    mergedSequence = []

    while len(sequence1) > 0 and len(sequence2) > 0:
        if sequence1[0] < sequence2[0]:
            mergedSequence.append(sequence1.pop(0))
        else:
            mergedSequence.append(sequence2.pop(0))

    mergedSequence.extend(sequence1)
    mergedSequence.extend(sequence2)

    return mergedSequence


list1 = ["AAB", "A", "BB", "BBC"]

print(sort(list1))

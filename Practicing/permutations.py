def createAllPermutations(sequence):
    mode = str(type(sequence))

    n = len(sequence)

    if n == 0:
        return []
    elif n == 1:
        return sequence
    elif n == 2:
        if mode == "<class 'list'>":
            return [sequence, [sequence[1], sequence[0]]]
        elif mode == "<class 'str'>":
            return [sequence, sequence[1] + sequence[0]]
    else:
        perms = []
        subperms = createAllPermutations(sequence[1:])

        for subperm in subperms:
            for i in range(len(subperm) + 1):
                if mode == "<class 'list'>":
                    newPerm = subperm[:i] + [sequence[0]] + subperm[i:]
                elif mode == "<class 'str'>":
                    newPerm = subperm[:i] + sequence[0] + subperm[i:]

                if newPerm not in perms:
                    perms.append(newPerm)

        return perms

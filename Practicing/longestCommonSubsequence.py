
# Not working!!

def main():
    sequences = getInputs()
    print(lcs(sequences))

def getInputs():
    return [input(), input()]

def lcs(sequences):
    def bySize(x):
        return len(x)
    sequences.sort(key=bySize)

    subsequences = set()
    commonElements = set(sequences[0]) & set(sequences[1])

    return sequences

main()

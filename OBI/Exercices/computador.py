def main():
    n, m = map(lambda x: int(x), input().split())

    # store the instructions and calculate single elements when requested
    # for each instruction:
        # is the requested element inside the current range?
            # startValue = starting value of the range
            # startIndex = starting index of the range
            # valueRequested += startValue - abs(startIndex - requested index)

    instructions = []
    # calculated = {}

    for i in range(m):
        newInstrucion = tuple(map(lambda x: int(x), input().split()))

        if newInstrucion[0] == 3:
            value = 0
            requestedIndex = newInstrucion[1] - 1

            for j in range(len(instructions) - 1, -1, -1):
                inst = instructions[j]

                # if (requestedIndex, j) in calculated:
                #     value += calculated[(requestedIndex, j)]
                #     break

                mode = inst[0]
                startIndex = inst[1] - 1
                startValue = inst[2]

                if mode == 1: # going right
                    if startIndex <= requestedIndex <= (startIndex + startValue): # inside range
                        value += startValue - (requestedIndex - startIndex)

                else: # going left
                    if (startIndex - startValue) <= requestedIndex <= startIndex: # inside range
                        value += startValue - (startIndex - requestedIndex)

            # calculated[(requestedIndex, len(instructions) - 1)] = value
            print(value)

        else:
            instructions.append((newInstrucion))

main()

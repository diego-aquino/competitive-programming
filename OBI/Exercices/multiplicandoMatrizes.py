def multiply(matrix1, matrix2):
    n1, m1 = len(matrix1), len(matrix1[0])
    n2, m2 = len(matrix2), len(matrix2[0])

    finalMatrix = []

    for i in range(n1):
        finalMatrix.append([])

        for j in range(m1):
            finalMatrix[i].append(0)

            for w in range(m1):
                finalMatrix[i][j] += matrix1[i][w] * matrix2[w][j]

    return finalMatrix

a = [
    [1, 1, 3],
    [1, 4, 1]
]

b = [
    [1, 2, 1],
    [3, 6, 3],
    [4, 7, 4],
]

for row in multiply(a, b):
    print(row)

def printMat(mat):
   for row in mat:
      print(row)

n = 4

mat = []
for i in range(n):
   mat.append([])

for i in range(n):
   for j in range(n):
      mat[i].append(-1)

x, y, peso = int(input()), int(input()), int(input())
mat[x][y] = peso
mat[y][x] = peso

printMat(mat)


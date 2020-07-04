from math import ceil

def main():
   n, m = getInputs()
   print(getMoves(n, m))

def getInputs():
   inputs = input().split()
   return int(inputs[0]), int(inputs[1])

def oldGetMoves(n, m):
   if n == m:
      moves = 0
   elif n > m:
      moves = n - m
   else:
      startingPoint = m

      while startingPoint > n and startingPoint > 1:
         startingPoint = ceil(startingPoint / 2)
      
      moves = n - startingPoint
      currentPoint = startingPoint

      while currentPoint < m:
         currentPoint *= 2
         moves += 1
      
      if currentPoint > m:
         moves += currentPoint - m

   return moves

def getMoves(n, m, moves=0):
   if n == m:
      return 0
   elif n > m:
      return n - m
   else:

main()

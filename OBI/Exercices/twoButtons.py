from math import ceil

def main():
   n, m = input().split()
   print(getMoves(int(n), int(m)))

def getMoves(n, m):
   if n == m:
      return 0
   elif n > m:
      return n - m
   else:
      method1, method2 = tryMethod(1, n, m), tryMethod(2, n, m)

      if method1 < method2:
         return method1
      else:
         return method2

def tryMethod(mode, n, m):
   if mode == 1:
      startingPoint = m

      while startingPoint > 1 and startingPoint > n:
         startingPoint = ceil(startingPoint / 2)

      moves = n - startingPoint

      currentPoint = startingPoint

      while currentPoint < m:
         currentPoint *= 2
         moves += 1
      
      if currentPoint > m:
         moves += currentPoint - m
   
   else:
      endPoint = n
      moves = 0

      while endPoint < m:
         endPoint *= 2
         moves += 1
      
      if endPoint > m:
         moves += endPoint - m
      
   return moves

main()

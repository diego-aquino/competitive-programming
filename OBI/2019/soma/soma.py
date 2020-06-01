def main():
   n, k, rectagle = getInputs()
   print(subrectangles(n, k, rectagle))

def getInputs():
   n, k = input().split()
   rectagle = input().split()

   return int(n), int(k), rectagle

def subrectangles(n, k, rectagle):
   subrectangles = 0

   for i in range(n):
      total = 0
      for j in range(i, n):
         total += int(rectagle[j])

         if total == k:
            subrectangles += 1
         elif total > k:
            break

   return subrectangles

main()

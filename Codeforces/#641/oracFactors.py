def main():
   numberOfCases = int(input())

   cases = getCases(numberOfCases)

   for case in cases:
      finalN = getFinalN(*case)
      print(finalN)

def getCases(numberOfCases):
   cases = []

   for i in range(numberOfCases):
      newCase = input().split()

      for j in range(2):
         newCase[j] = int(newCase[j])

      cases.append(newCase)

   return cases

def getFinalN(n, k):
   while k > 0:
      smallestDivisor = 1

      for i in range(2, n + 1):
         if n % i == 0:
            smallestDivisor = i
            break

      n += smallestDivisor
      k -= 1

   return n

main()

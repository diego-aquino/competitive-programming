def main():
   numberOfCases = int(input())

   cases = getCases(numberOfCases)

   for i in range(numberOfCases):
      countdowns = getCountdowns(cases[i])
      print("Case #{}: {}".format(i + 1, countdowns))

def getCases(numberOfCases):
   cases = []

   for i in range(numberOfCases):
      n, k = input().split()
      numbers = input().split()

      for j in range(int(n)):
         numbers[j] = int(numbers[j])
      
      cases.append((int(n), int(k), numbers))

   return cases

def getCountdowns(case):
   # sortedNumbers = sort(case[2])
   countdowns = 0

   skipUntil = -1
   for i in range(case[0]):
      if i <= skipUntil:
         continue
      else:
         if case[2][i] == case[1]:
            for j in range(i + 1, case[0]):
               if case[2][j] == case[2][i] - (j - i):
                  if case[2][j] == 1:
                     countdowns += 1
                     skipUntil = j
               else: break

   return countdowns

main()

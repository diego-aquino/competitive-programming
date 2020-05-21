def main():
   numberOfCases = int(input())
   cases = getCases(numberOfCases)

   for i in range(numberOfCases):
      totalSweet = getTotalSweet(cases[i])
      print("Case #{}: {}".format(i + 1, totalSweet))

def getCases(numberOfCases):
   cases = []

   for i in range(numberOfCases):
      n, q = input().split()
      n, q = int(n), int(q)

      array = []
      for number in input().split():
         array.append(int(number))

      operations = []
      for j in range(q):
         newOp = input().split()

         for k in range(1, 3):
            newOp[k] = int(newOp[k])

         operations.append(newOp)
      
      cases.append((n, q, array, operations))

   return cases

def getTotalSweet(case):
   totalSum = 0

   for operation in case[3]:
      if operation[0] == "Q":
         subarray = case[2][operation[1] - 1:operation[2]]

         factor = 1
         for i in range(len(subarray)):
            totalSum += subarray[i] * (i + 1) * factor

            if factor == 1:
               factor = -1
            else:
               factor = 1
      else:
         case[2][operation[1] - 1] = operation[2]

   return totalSum

main()

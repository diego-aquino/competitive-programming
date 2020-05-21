def main():
   numberOfCases = int(input())

   cases = getCases(numberOfCases)

   for i in range(numberOfCases):
      perfects = getPerfects(cases[i])
      print("Case #{}: {}".format(i + 1, perfects))

def getCases(numberOfCases):
   cases = []

   for i in range(numberOfCases):
      n = int(input())

      array = []
      for number in input().split():
         array.append(int(number))
      
      cases.append((n, array))
   
   return cases

def getPerfects(case):
   perfects = 0

   for i in range(case[0]):
      for j in range(i, case[0]):
         if i == j:
            total = case[1][i]
         else:
            subarray = case[1][i:j + 1]
            total = sum(subarray)

         if total >= 0 and (total ** 0.5).is_integer():
            perfects += 1

   return perfects

# def mergeSum(elementList):
#    n = len(elementList)

#    if n == 1:
#       return elementList[0]
#    elif n == 2:
#       return elementList[0] + elementList[1]
#    else:
#       return mergeSum(elementList[:n//2]) + mergeSum(elementList[n//2:])

main()

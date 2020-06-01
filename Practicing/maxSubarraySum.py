def main():
   array = getArray()
   maxSum = getMaxSum(array)
   print(maxSum)

def getArray():
   array = input().split()
   for i in range(len(array)):
      array[i] = int(array[i])

   return array

def getMaxSum(array):
   if len(array) == 0:
      return 0

   best, currentSum = 0, 0
   for i in range(len(array)):
      currentSum = max(array[i], currentSum + array[i])
      best = max(best, currentSum)

   return best

   # maxSum = array[0]

   # for i in range(len(array)):
   #    currentSum = 0
   #    for j in range(i, len(array)):
   #       currentSum += array[j]
   #       maxSum = max(maxSum, currentSum)

   # return maxSum

main()

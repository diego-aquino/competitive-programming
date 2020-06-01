def main():
   n, numbers = getInputs()
   print(getMaxMarked(n, numbers))

def getInputs():
   n = int(input())

   numbers = []
   for i in range(n):
      numbers.append(int(input()))

   return n, numbers

def getMaxMarked(n, numbers):
   uniqueNumbers = getUniqueNumbers(numbers)

   maxMarked = 0

   marked = [0]
   for i in range(len(uniqueNumbers)):
      for j in range(i + 1, len(uniqueNumbers)):
         for number in numbers:
            if number == uniqueNumbers[i] or number == uniqueNumbers[j]:
               if number != marked[-1]:
                  marked.append(number)
      
         if len(marked) - 1 > maxMarked:
            maxMarked = len(marked) - 1

         marked = [0]

   if maxMarked > 0:
      return maxMarked
   else:
      return 1

def getUniqueNumbers(numbers):
   uniqueNumbers = []

   for number in numbers:
      if number not in uniqueNumbers:
         uniqueNumbers.append(number)

   return uniqueNumbers

main()

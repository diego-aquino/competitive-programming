def main():
   pairsToCombine = getInputs()

   for pair in pairsToCombine:
      combinedString = getCombinedString(pair)
      print(combinedString)

def getInputs():
   numberOfCases = int(input())

   pairs = []
   for i in range(numberOfCases):
      newPair = input().split()
      pairs.append(newPair)

   return pairs

def getCombinedString(pair):
   combinedString = ""
   index = 0

   while len(pair[0]) > 0 and len(pair[1]) > 0:
      combinedString += pair[index][0]
      pair[index] = pair[index][1:]

      if index == 0:
         index = 1
      else:
         index = 0

   combinedString += pair[0]
   combinedString += pair[1]

   return combinedString

main()

def main():
   numberOfCases = int(input())

   cases = getCases(numberOfCases)

   for case in cases:
      maxModels = getMaxModels(*case)
      print(maxModels)

def getCases(numberOfCases):
   cases = []

   for i in range(numberOfCases):
      numberOfModels = int(input())

      modelSizes = input().split()

      for j in range(numberOfModels):
         modelSizes[j] = int(modelSizes[j])

      cases.append([numberOfModels, modelSizes])

   return cases

def getMaxModels(numberOfModels, modelSizes):
   modelsPairs = []

   for i in range(numberOfModels):
      modelsPairs.append((modelSizes[i], i))

   modelsPairs.sort(key=getIndex)
   modelsPairs.sort(key=getSize)

   modelsToBuy = []

   while len(modelsPairs) > 0:
      if len(modelsToBuy) == 0:
         modelsToBuy.append(modelsPairs[0])
      else:
         if (modelsPairs[0][1] + 1) % (modelsToBuy[-1][1] + 1) == 0 \
            and modelsPairs[0][0] > modelsToBuy[-1][0]:
            modelsToBuy.append(modelsPairs[0])

      modelsPairs.pop(0)

   return len(modelsToBuy)

def getIndex(tuple):
   return tuple[1]

def getSize(tuple):
   return tuple[0]

main()

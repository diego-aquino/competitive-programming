def main():
   cases = getCases()

   for case in cases:
      numberOfTrades = getMaxNumberOfTrades(case)
      print(numberOfTrades)

def getCases():
   cases = []
   while True:
      amountOfCardsEach = input()

      if amountOfCardsEach == "0 0": break
      else:
         currentCase = []

         for i in range(2):
            currentPlayerCards = input().split()

            for j in range(len(currentPlayerCards)):
               currentPlayerCards[j] = int(currentPlayerCards[j])

            currentCase.append(currentPlayerCards)

         cases.append(currentCase)

   return cases

def getMaxNumberOfTrades(case):
   validCards = []

   for playerNum in range(2):
      validPlayerCards = []

      for cardNum in range(len(case[playerNum])):
         currentCardValue = case[playerNum][cardNum]

         if playerNum == 1:
            nextPlayerNum = 0
         elif playerNum == 0:
            nextPlayerNum = 1

         if not find(currentCardValue, case[nextPlayerNum]) \
            and not find(currentCardValue, validPlayerCards):
            validPlayerCards.append(currentCardValue)

      validCards.append(validPlayerCards)

   if len(validCards[0]) < len(validCards[1]):
      return len(validCards[0])
   else:
      return len(validCards[1])

def find(element, listOfElements):
   low = 0
   high = len(listOfElements) - 1

   while low <= high:
      midIndex = (high + low) // 2
      midElement = listOfElements[midIndex]

      if element > midElement:
         low = midIndex + 1
      elif element < midElement:
         high = midIndex - 1
      else:
         return True

   return False

main()

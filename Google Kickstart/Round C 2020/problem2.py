def main():
   numberOfCases = int(input())

   cases = getCases(numberOfCases)

   for i in range(numberOfCases):
      order = getBuildingOrder(cases[i])
      print("Case #{}: {}".format(i + 1, order))

def getCases(numberOfCases):
   cases = []

   for i in range(numberOfCases):
      r, c = input().split()
      r, c = int(r), int(c)

      wall = []
      for j in range(r):
         wall.append(input())

      cases.append((r, c, wall))

   return cases

def getBuildingOrder(case):
   uniqueLetters = getUniqueLetters(case) # ZOAM

   order = ""

   for j in range(len(uniqueLetters)): # For each order position
      onTop = False

      for i in range(len(uniqueLetters)):
         if uniqueLetters[i] not in order:
            if isOnTop(uniqueLetters[i], case):
               removeLetter(uniqueLetters[i], case[2])

               order += uniqueLetters[i]
               onTop = True
               break
      
      if onTop == False:
         return -1 

   return reverse(order)

def getUniqueLetters(case):
   uniqueLetters = ""

   for i in range(case[0]):
      for j in range(case[1]):
         if case[2][i][j] not in uniqueLetters:
            uniqueLetters += case[2][i][j]

   return uniqueLetters

def isOnTop(letter, case):
   for i in range(case[0]):
      for j in range(case[1]):
         currentLetter = case[2][i][j]
         if currentLetter == letter and i > 0:
            letterAbove = case[2][i - 1][j]
            if letterAbove != currentLetter and letterAbove != " ":
               return False
   
   return True

def removeLetter(letter, wall):
   for i in range(len(wall)):
      wall[i] = wall[i].replace(letter, " ")

def reverse(string):
   reversedStr = ""

   for i in range(-1, - len(string) - 1, -1):
      reversedStr += string[i]

   return reversedStr

main()

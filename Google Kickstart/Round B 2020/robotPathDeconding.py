def main():
   numberOfCases = int(input())
   cases = getCases(numberOfCases)

   for i in range(numberOfCases):
      caseProgram = cases[i]
      finalPosition = getFinalPosition(caseProgram)

      print("Case #{}: {} {}".format(i + 1, *finalPosition))

def getCases(numberOfCases):
   cases = []
   for i in range(numberOfCases):
      cases.append(input())

   return cases

def getFinalPosition(program):
   coords = [1, 1]
   moves = getMoves(program)

   coords[0] += moves["E"] - moves["W"] # Horizontal overall move
   coords[1] += moves["S"] - moves["N"] # Vertical overall move

   for i in range(2):
      while coords[i] < 1:
         coords[i] += 10 ** 9
      while coords[i] > 10 ** 9:
         coords[i] -= 10 ** 9

   return coords

def getMoves(program):
   moves = {"N": 0, "S": 0, "E": 0, "W": 0}

   chrToSkip = 0

   for i in range(len(program)):
      if chrToSkip > 0:
         chrToSkip -= 1
         continue
      else:
         if program[i].isnumeric():
            moveToRepeatStr = ""

            nestedRepeats = 0
            chrToSkip = 2

            while True:
               currentChr = program[i + chrToSkip]

               if currentChr == ")":
                  if nestedRepeats > 0:
                     nestedRepeats -= 1
                     moveToRepeatStr += currentChr
                  else:
                     break
               else:
                  if currentChr == "(":
                     nestedRepeats += 1

                  moveToRepeatStr += currentChr

               chrToSkip += 1

            movesToRepeat = {"N": 0, "S": 0, "E": 0, "W": 0}

            if moveToRepeatStr.count("(") > 0:
               countedMoves = getMoves(moveToRepeatStr)

               for direction in ["N", "S", "E", "W"]:
                  movesToRepeat[direction] += countedMoves[direction]
            else:
               for direction in ["N", "S", "E", "W"]:
                  movesToRepeat[direction] = moveToRepeatStr.count(direction)

            for direction in ["N", "S", "E", "W"]:
               moves[direction] += movesToRepeat[direction] * int(program[i])

         else:
            moves[program[i]] += 1

   return moves

main()

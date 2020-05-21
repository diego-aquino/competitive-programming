def getScore(_inputScore):
   return _inputScore[0] * _inputScore[1]

def parseInputScore(inputScore):
   inputScore = inputScore.split(" ")

   for i in range(2):
      inputScore[i] = float(inputScore[i])

   return inputScore


numberOfTestCases = int(input())
message = ""

for testCase in range(numberOfTestCases):
   joaosScore = 0
   mariasScore = 0

   for johnsPitch in range(3):
      caseResult = input()
      joaosScore += getScore(parseInputScore(caseResult))

   for mariasPitch in range(3):
      caseResult = input()
      mariasScore += getScore(parseInputScore(caseResult))

   if (joaosScore > mariasScore):
      message += "JOAO\n"
   else:
      message += "MARIA\n"

print(message, end="")

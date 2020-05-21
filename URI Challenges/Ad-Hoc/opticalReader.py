def main():
   cases = getCases()

   for case in cases:
      markedAlternatives = getAlternatives(case)

      for alternative in markedAlternatives:
         print(alternative)

def getCases():
   cases = []

   while True:
      numberOfQuestions = int(input())

      if numberOfQuestions:
         currentCase = []
         for i in range(numberOfQuestions):
            currentCase.append(input())

         cases.append(currentCase)

      else: break

   return cases

def getAlternatives(case):
   answerDatabase = ["A", "B", "C", "D", "E"]

   caseAnswers = []

   for question in case:
      question = question.split()

      markedAlternatives = []
      for alternative in question:
         markedAlternatives.append(int(alternative) <= 127)

      if markedAlternatives.count(True) == 1:
         index = markedAlternatives.index(True)
         caseAnswers.append(answerDatabase[index])
      else:
         caseAnswers.append("*")

   return caseAnswers

main()

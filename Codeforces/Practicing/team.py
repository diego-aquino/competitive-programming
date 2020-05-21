def main():
   numberOfProblems = int(input())

   problems = getInputProblems(numberOfProblems)

   problemsToSolve = 0
   for problem in problems:
      if solve(problem):
         problemsToSolve += 1

   print(problemsToSolve)   

def getInputProblems(n):
   problems = []
   for i in range(n):
      problems.append(input())
   
   return problems

def solve(problem):
   return problem.count("1") >= 2

main()

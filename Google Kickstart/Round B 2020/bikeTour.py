def main():
   numberOfCases = int(input())

   cases = getCases(numberOfCases)

   for i in range(numberOfCases):
      peaks = getPeaks(cases[i][0], cases[i][1])
      print("Case #{}: {}".format(i + 1, peaks))

def getCases(numberOfCases):
   cases = []

   for i in range(numberOfCases):
      N = int(input())
      checkpoints = input().split()

      for i in range(N):
         checkpoints[i] = int(checkpoints[i])

      cases.append((N, checkpoints))

   return cases

def getPeaks(numberOfCheckpoints, caseCheckpoints):
   peaks = 0

   for j in range(1, numberOfCheckpoints - 1):
      if caseCheckpoints[j - 1] < caseCheckpoints[j] > caseCheckpoints[j + 1]:
         peaks += 1

   return peaks

main()

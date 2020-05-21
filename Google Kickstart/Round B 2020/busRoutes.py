def main():
   numberOfCases = int(input())

   cases = getCases(numberOfCases)

   for i in range(numberOfCases):
      latestDay = getLastestDay(cases[i][0], cases[i][1], cases[i][2])
      print("Case #{}: {}".format(i + 1, latestDay))

def getCases(numberOfCases):
   cases = []

   for i in range(numberOfCases):
      cases.append((getCaseInput()))

   return cases

def getCaseInput():
   numberOfRoutes, deadline = input().split()
   routeDays = input().split()

   numberOfRoutes, deadline = int(numberOfRoutes), int(deadline)

   for j in range(numberOfRoutes):
      routeDays[j] = int(routeDays[j])

   return numberOfRoutes, deadline, routeDays

def getLastestDay(numberOfRoutes, deadline, routeDays):
   multiples = getRouteMultiples(deadline, routeDays)
   latestDays = getHighestDays(numberOfRoutes, multiples)

   # For each route, starting from the second-to-last and going all the way down to i == 0
   for i in range(numberOfRoutes - 2, -1, -1):
      currentRoutePossibleDays = multiples[i]
      nextRouteDay = latestDays[i + 1]

      # For multiple in route, in descending order
      low = 0
      high = len(currentRoutePossibleDays) - 1

      while True:
         middle = (high + low) // 2

         prospectiveDay = currentRoutePossibleDays[middle]

         try:
            nextMultiple = currentRoutePossibleDays[middle + 1]
         except:
            nextMultiple = None

         if prospectiveDay <= nextRouteDay:
            if nextMultiple:
               if nextMultiple > nextRouteDay:
                  latestDays[i] = prospectiveDay
                  break
               else:
                  low = middle + 1
            else:
               latestDays[i] = prospectiveDay
               break
         else:
            high = middle - 1

   # # Setting the lowest value possible for each day after the first one
   # for i in range(1, numberOfRoutes):
   #    while latestDays[i] - routeDays[i] >= latestDays[i - 1]:
   #       latestDays[i] -= routeDays[i]

   return latestDays[0]

def getRouteMultiples(deadline, routeDays):
   multiples = []
   for day in routeDays:
      multiples.append(range(0, deadline + 1, day))

   return multiples

def getHighestDays(numberOfRoutes, multiples):
   latestDays = []
   for i in range(numberOfRoutes):
      latestDays.append(multiples[i][-1])

   return latestDays

main()

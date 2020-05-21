def main():
   n = int(input())
   drifts = getDrifts(n)
   print(getDriftsToBeCreated(drifts))

def getDrifts(n):
   drifts = []
   for i in range(n):
      newDrift = input().split()

      newDrift[0] = int(newDrift[0])
      newDrift[1] = int(newDrift[1])

      drifts.append(newDrift)

   return drifts

def getDriftsToBeCreated(drifts):
   if len(drifts) == 1:
      return 0
   else:
      initialAmountOfDrifts = len(drifts)

      for currentDrift in drifts:
         if not reachable(drifts, currentDrift):
            reach(drifts, currentDrift)

      return len(drifts) - initialAmountOfDrifts

def reachable(drifts, currentDrift):
   for comparingDrift in drifts:
      if comparingDrift != currentDrift:
         if comparingDrift[0] == currentDrift[0] or comparingDrift[1] == currentDrift[1]:
            return True

   return False

def reach(drifts, currentDrift):
   closestDrift = getClosestDrift(drifts, currentDrift)
   
   if closestDrift[0] < currentDrift[0]:
      validRange = range(closestDrift[0] + 1, currentDrift[0])
   else:
      validRange = range(currentDrift[0] + 1, closestDrift[0])

   for x in validRange:
      newDrift = [x, currentDrift[1]]
      if newDrift not in drifts:
         drifts.append(newDrift)
   
   if closestDrift[1] < currentDrift[1]:
      validRange = range(closestDrift[1] + 1, currentDrift[1] + 1)
   else:
      validRange = range(currentDrift[1] + 1, closestDrift[1] + 1)

   for y in validRange:
      newDrift = [closestDrift[0], y]
      if newDrift not in drifts:
         drifts.append(newDrift)

def getClosestDrift(drifts, currentDrift):
   if len(drifts) == 2:
      if drifts[0] == currentDrift:
         return drifts[1]
      else:
         return drifts[0]
   else:
      radius = 0

      while True:
         radius += 1

         for prospectiveDrift in drifts:
            if prospectiveDrift[0] == currentDrift[0] - radius \
               or prospectiveDrift[0] == currentDrift[0] + radius:
               if prospectiveDrift[1] == currentDrift[1] - radius \
                  or prospectiveDrift[1] == currentDrift[1] + radius:
                  return prospectiveDrift

main()

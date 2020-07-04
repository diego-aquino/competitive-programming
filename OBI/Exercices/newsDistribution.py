def main():
   n, m, groups = getInputs()
   
   output = ""
   for i in range(n):   
      output += str(distributeNews(n, m, groups.copy(), i)) + " "

   print(output[:-1])

def getInputs():  
   n, m = input().split()
   n, m = int(n), int(m)

   groups = []
   for i in range(m):
      groupUsers = input().split()
      groupUsers.pop(0)

      newGroup = [0] * n

      for user in groupUsers:
         newGroup[int(user) - 1] = 1

      groups.append(newGroup)

   return n, m, groups

def distributeNews(n, m, groups, user):
   for i in range(m):
      groups[i] = groups[i].copy()

      if groups[i][user] == 1:
         groups[i][user] = 2

   while isThere2(n, m, groups):
      for i in range(m):         
         if someoneKnows(n, groups[i]):
            for j in range(n):
               if groups[i][j] == 2:
                  groups[i][j] = 3
               elif groups[i][j] == 1:
                  groups[i][j] = 2

      for j in range(n):
         knows = False

         for i in range(m):
            if groups[i][j] == 2:
               knows = True
               break
         
         if knows:
            for i in range(m):
               if groups[i][j] == 1:
                  groups[i][j] = 2

   informedUsers = getAmountOfInformedUsers(n, m, groups)
   
   if informedUsers > 0:
      return informedUsers
   else:
      return 1

def isThere2(n, m, groups):
   for i in range(m):
      for j in range(n):
         if groups[i][j] == 2:
            return True

   return False

def someoneKnows(n, currentGroup):
   for j in range(n):
      if currentGroup[j] == 2:
         return True
   
   return False

def getAmountOfInformedUsers(n, m, groups):
   total = 0
   for j in range(n):
      for i in range(m):
         if groups[i][j] == 3:
            total += 1
            break

   return total

main()

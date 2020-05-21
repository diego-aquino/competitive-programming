def getTheGreatestNumber(arrayOfNumbers):
   a, b, c = arrayOfNumbers[0], arrayOfNumbers[1], arrayOfNumbers[2]

   firstGreatest = (a + b + abs(a - b)) / 2

   finalGreatest = 0

   if (firstGreatest == a):
      finalGreatest = (a + c + abs(a - c)) / 2
   else:
      finalGreatest = (b + c + abs(b - c)) / 2

   return round(finalGreatest)


inputNumbers = input()

inputNumbers = inputNumbers.split(" ")

for i in range(len(inputNumbers)):
   inputNumbers[i] = int(inputNumbers[i])

print("{} é o maior.".format(getTheGreatestNumber(inputNumbers)))

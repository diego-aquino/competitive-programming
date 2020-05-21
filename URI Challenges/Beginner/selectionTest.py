inputNumbersAsString = input()

inputNumbersAsArrayString = inputNumbersAsString.split(" ")

formatedNumbers = []

for i in range(len(inputNumbersAsArrayString)):
   formatedNumbers.append(eval(inputNumbersAsArrayString[i]))

a = formatedNumbers[0]
b = formatedNumbers[1]
c = formatedNumbers[2]
d = formatedNumbers[3]

def requirement1():
   return (b > c) and (d > a)

def requirement2():
   return (c + d) > (a + b)

def requirement3():
   return (c > 0) and (d > 0)

def requirement4():
   return (a % 2 == 0)

def areAllRequirementsMet():
   return requirement1() and requirement2() and requirement3() and requirement4()

if (areAllRequirementsMet()):
   print("Valores aceitos")
else:
   print("Valores nao aceitos")

def main():
   numbers = getInputs()

   for num in numbers:
      totalOfLeds = getTotalLeds(num)
      print("{} leds".format(totalOfLeds))

def getInputs():
   numberOfCases = eval(input())

   numbers = []
   for i in range(numberOfCases):
      newNumber = int(input())
      numbers.append(newNumber)

   return numbers

def getTotalLeds(number):
   amountOfLeds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

   total = 0
   for alg in str(number):
      total += amountOfLeds[int(alg)]

   return total

main()

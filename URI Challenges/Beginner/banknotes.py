import math

value = int(input())

finalMessage = "{}\n".format(value)


if (value >= 100):
   numberOfHundreds = math.floor(value / 100)
   finalMessage += "{} nota(s) de R$ 100,00\n".format(numberOfHundreds)

   value -= numberOfHundreds * 100
else:
   finalMessage += "0 nota(s) de R$ 100,00\n"


if (value >= 50):
   numberOfFifties = math.floor(value / 50)
   finalMessage += "{} nota(s) de R$ 50,00\n".format(numberOfFifties)

   value -= numberOfFifties * 50
else:
   finalMessage += "0 nota(s) de R$ 50,00\n"


if (value >= 20):
   numberOfTwenties = math.floor(value / 20)
   finalMessage += "{} nota(s) de R$ 20,00\n".format(numberOfTwenties)

   value -= numberOfTwenties * 20
else:
   finalMessage += "0 nota(s) de R$ 20,00\n"


if (value >= 10):
   numberOfTens = math.floor(value / 10)
   finalMessage += "{} nota(s) de R$ 10,00\n".format(numberOfTens)

   value -= numberOfTens * 10
else:
   finalMessage += "0 nota(s) de R$ 10,00\n"


if (value >= 5):
   numberOfFives = math.floor(value / 5)
   finalMessage += "{} nota(s) de R$ 5,00\n".format(numberOfFives)

   value -= numberOfFives * 5
else:
   finalMessage += "0 nota(s) de R$ 5,00\n"


if (value >= 2):
   numberOfTwos = math.floor(value / 2)
   finalMessage += "{} nota(s) de R$ 2,00\n".format(numberOfTwos)

   value -= numberOfTwos * 2
else:
   finalMessage += "0 nota(s) de R$ 2,00\n"


if (value >= 1):
   numberOfOnes = value
   finalMessage += "{} nota(s) de R$ 1,00".format(numberOfOnes)

   value = 0
else:
   finalMessage += "0 nota(s) de R$ 1,00"


print(finalMessage)

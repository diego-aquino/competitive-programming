import math

value = float(input())

def roundValue():
   return float("%.2f" % (value))

value = roundValue()

finalMessage = "NOTAS:\n"

# ==============================================================================

if (value >= 100):
   numberOfCurrentUnit = math.floor(value / 100)
   finalMessage += "{} nota(s) de R$ 100.00\n".format(numberOfCurrentUnit)

   value -= numberOfCurrentUnit * 100
else:
   finalMessage += "0 nota(s) de R$ 100.00\n"

value = roundValue()

if (value >= 50):
   numberOfCurrentUnit = math.floor(value / 50)
   finalMessage += "{} nota(s) de R$ 50.00\n".format(numberOfCurrentUnit)

   value -= numberOfCurrentUnit * 50
else:
   finalMessage += "0 nota(s) de R$ 50.00\n"

value = roundValue()

if (value >= 20):
   numberOfCurrentUnit = math.floor(value / 20)
   finalMessage += "{} nota(s) de R$ 20.00\n".format(numberOfCurrentUnit)

   value -= numberOfCurrentUnit * 20
else:
   finalMessage += "0 nota(s) de R$ 20.00\n"

value = roundValue()

if (value >= 10):
   numberOfCurrentUnit = math.floor(value / 10)
   finalMessage += "{} nota(s) de R$ 10.00\n".format(numberOfCurrentUnit)

   value -= numberOfCurrentUnit * 10
else:
   finalMessage += "0 nota(s) de R$ 10.00\n"

value = roundValue()

if (value >= 5):
   numberOfCurrentUnit = math.floor(value / 5)
   finalMessage += "{} nota(s) de R$ 5.00\n".format(numberOfCurrentUnit)

   value -= numberOfCurrentUnit * 5
else:
   finalMessage += "0 nota(s) de R$ 5.00\n"

value = roundValue()

if (value >= 2):
   numberOfCurrentUnit = math.floor(value / 2)
   finalMessage += "{} nota(s) de R$ 2.00\n".format(numberOfCurrentUnit)

   value -= numberOfCurrentUnit * 2
else:
   finalMessage += "0 nota(s) de R$ 2.00\n"

value = roundValue()

# ==============================================================================

finalMessage += "MOEDAS:\n"

if (value >= 1):
   numberOfCurrentUnit = math.floor(value)
   finalMessage += "{} moeda(s) de R$ 1.00\n".format(numberOfCurrentUnit)

   value -= numberOfCurrentUnit
else:
   finalMessage += "0 moeda(s) de R$ 1.00\n"

value = roundValue()

if (value >= 0.5):
   numberOfCurrentUnit = math.floor(value / 0.5)
   finalMessage += "{} moeda(s) de R$ 0.50\n".format(numberOfCurrentUnit)

   value -= numberOfCurrentUnit * 0.5
else:
   finalMessage += "0 moeda(s) de R$ 0.50\n"

value = roundValue()

if (value >= 0.25):
   numberOfCurrentUnit = math.floor(value / 0.25)
   finalMessage += "{} moeda(s) de R$ 0.25\n".format(numberOfCurrentUnit)

   value -= numberOfCurrentUnit * 0.25
else:
   finalMessage += "0 moeda(s) de R$ 0.25\n"

value = roundValue()

if (value >= 0.1):
   numberOfCurrentUnit = math.floor(value / 0.1)
   finalMessage += "{} moeda(s) de R$ 0.10\n".format(numberOfCurrentUnit)

   value -= numberOfCurrentUnit * 0.1
else:
   finalMessage += "0 moeda(s) de R$ 0.10\n"

value = roundValue()

if (value >= 0.05):
   numberOfCurrentUnit = math.floor(value / 0.05)
   finalMessage += "{} moeda(s) de R$ 0.05\n".format(numberOfCurrentUnit)

   value -= numberOfCurrentUnit * 0.05
else:
   finalMessage += "0 moeda(s) de R$ 0.05\n"

value = roundValue()

if (value >= 0.01):
   numberOfCurrentUnit = math.floor(value / 0.01)
   finalMessage += "{} moeda(s) de R$ 0.01".format(numberOfCurrentUnit)

   value = 0
else:
   finalMessage += "0 moeda(s) de R$ 0.01"

value = roundValue()

# ==============================================================================

print(finalMessage)

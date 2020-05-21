inputNumbers = input()

inputNumbers = inputNumbers.split(" ")

for i in range(0, len(inputNumbers)):
   inputNumbers[i] = float(inputNumbers[i])

a = inputNumbers[0]
b = inputNumbers[1]
c = inputNumbers[2]

delta = (b**2) - (4*a*c)

if (delta < 0 or a == 0):
   print("Impossivel calcular")
else:
   r1 = (-b + delta**0.5) / (2*a)
   r2 = (-b - delta**0.5) / (2*a)

   print("R1 = {:.5f}\nR2 = {:.5f}".format(r1, r2))

m = 1

def getNewPrime():
   global m

   while True:
      prime = True
      m += 1

      for divisor in range(2, m):
         if m % divisor == 0:
            prime = False
            break

      if prime:
         return m

message = ""

while True:
   inputNumber = int(input())

   if inputNumber == 0:
      break

   positions = []

   for i in range(inputNumber):
      positions.append(i + 1)

   lastPoppedPosition = 0

   while True:
      prime = getNewPrime()
      popPosition = prime + lastPoppedPosition

      if popPosition > len(positions):
         popPosition = popPosition % len(positions)

      positions.pop(popPosition - 1)

      if len(positions) == 1:
         break

      lastPoppedPosition = popPosition

   message += str(positions[0]) + "\n"

print(message, end="")

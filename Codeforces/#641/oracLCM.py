def main():
   numIntegers = int(input())
   sequence = getSequence(numIntegers)

   mmcs = getMMCs(sequence, numIntegers)
   mdc = mdc(mmcs)

   print(mdc)

def getSequence(numIntegers):
   strSequence = input().split()

   for i in range(numIntegers):
      strSequence[i] = int(strSequence[i])

   return strSequence

def getMMCs(sequence, numIntegers):
   mmcs = []

   for i in range(numIntegers):
      for j in range(numIntegers):
         if i < j:
            mmcs.append(mmc(sequence[i], sequence[j]))

   return mmcs

def mmc(num1, num2):
   a, b = num1, num2

   while True:
      remainder = a % b
      a = b
      b = remainder

      if remainder == 0:
         break

   return (num1 * num2) / a

def mdc(sequence):
   resto = None

   while resto is not 0:
      resto = num1 % num2
      num1  = num2
      num2  = resto

   return num1

main()

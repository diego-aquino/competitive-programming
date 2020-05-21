def main():
   m, n = getInputs()

   if m % 2 == 0:
      total = (m // 2) * n
   elif n % 2 == 0:
      total = m * (n // 2)
   else:
      if m > 2:
         total = ((m // 2) * n) + (n // 2)
      elif n > 2:
         total = (m * (n // 2)) + (m // 2)
      else:
         total = 0

   print(round(total))

def getInputs():
   m, n = input().split()
   return int(m), int(n)

main()

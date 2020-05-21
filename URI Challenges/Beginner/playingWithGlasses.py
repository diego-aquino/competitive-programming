numberOfMoves = int(input())
coinPosition = input()

for i in range(numberOfMoves):
   move = int(input())

   if (move == 1):
      if (coinPosition == "A"):
         coinPosition = "B"
      elif (coinPosition == "B"):
         coinPosition = "A"
   elif (move == 2):
      if (coinPosition == "B"):
         coinPosition = "C"
      elif (coinPosition == "C"):
         coinPosition = "B"
   else:
      if (coinPosition == "A"):
         coinPosition = "C"
      elif (coinPosition == "C"):
         coinPosition = "A"

print(coinPosition)

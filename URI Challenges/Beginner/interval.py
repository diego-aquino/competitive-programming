number = float(input())

if (number >= 0 and number <= 25):
   print("Intervalo [0,25]")

elif (number > 25 and number <= 50):
   print("Intervalo (25,50]")

elif (number > 50 and number <= 75):
   print("Intervalo (50,75]")

elif (number > 75 and number <= 100):
   print("Intervalo (75,100]")

elif (number < 0 or number > 100):
   print("Fora de intervalo")

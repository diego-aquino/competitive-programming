letter = input()

spectre = "ABCDEFGHIJKLMNOPQRSTUVWXYZ["

for index in range(len(spectre)):
   if (letter < spectre[index]):
      print(index)
      break

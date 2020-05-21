message = ""

while True:
   sentence = input()

   if sentence == "*":
      break

   sentenceSplitToWords = sentence.split()

   initialLetter = sentenceSplitToWords[0][0]
   tautogram = True

   for word in sentenceSplitToWords:
      if initialLetter.lower() != word[0].lower():
         tautogram = False
         break

   if tautogram:
      message += "Y\n"
   else:
      message += "N\n"

print(message, end="")

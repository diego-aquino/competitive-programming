def main():
   numberOfWords = int(input())

   abreviatedWords = []
   for i in range(numberOfWords):
      abreviatedWords.append(abreviate(input()))

   for word in abreviatedWords:
      print(word)

def abreviate(word):
   n = len(word)

   if n > 10:
      return word[0] + str(n - 2) + word[-1]
   else:
      return word

main()

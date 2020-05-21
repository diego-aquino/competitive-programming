def main():
   strings = getInputStrings()

   for i in range(len(strings[0])):
      if strings[0][i] != strings[1][i]:
         print("{} ({})".format(strings[0][i], i))

def getInputStrings():
   strings = ["", ""]

   for i in range(2):
      numberOfLines = int(input())

      for j in range(numberOfLines):
         strings[i] += input() + "\n"

   return strings

main()

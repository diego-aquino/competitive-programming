def main():
   inputStrings = getInputStrings()

   for string in inputStrings:
      encryptedString = encrypt(string)
      print(encryptedString)

def getInputStrings():
   numberOfCases = int(input())

   strings = []
   for i in range(numberOfCases):
      strings.append(input())

   return strings

def encrypt(string):
   string = shiftPosition1(string)
   string = reverse(string)
   string = shiftPosition2(string)

   return string

def shiftPosition1(string):
   shiftedPositionsString = ""

   for character in string:
      if isLetter(character):
         shiftedPositionsString += chr(ord(character) + 3)
      else:
         shiftedPositionsString += character

   return shiftedPositionsString

def isLetter(character):
   position = ord(character)

   return 65 <= position <= 90 or 97 <= position <= 122

def reverse(string):
   reversedString = ""
   for i in range(len(string) - 1, -1, -1):
      reversedString += string[i]
   return reversedString

def shiftPosition2(string):
   n = len(string)

   halfShiftedPositionsString = string[:n//2]

   for character in string[n//2:]:
      halfShiftedPositionsString += chr(ord(character) - 1)

   return halfShiftedPositionsString

main()

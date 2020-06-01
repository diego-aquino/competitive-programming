def main():
   m, matriz = getInputs()

   finalMatriz = runWater(m, matriz)
   for line in finalMatriz:
      print(line)

def getInputs():
   n, m = map(lambda x: int(x), input().split())
   matriz = []
   for i in range(n):
      matriz.append(input())

   return m, matriz

def runWater(m, matriz):
   currentLine = 0

   while matriz[-1].count("o") == 0:
      prevCurrNextPair = getPrevCurrNextPair(m, matriz, currentLine)
      matriz[currentLine] = update(m, *prevCurrNextPair)

      currentLine += 1

   return matriz

def getPrevCurrNextPair(m, matriz, currentLine):
   prevCurrNextPair = ["", "", ""]

   for i in range(3):
      try:
         index = currentLine + i - 1
         if index < 0:
            raise Exception

         prevCurrNextPair[i] = matriz[index]
      except:
         prevCurrNextPair[i] = " " * m

   return prevCurrNextPair

def update(m, previusLine, line, nextLine):
   for i in range(0, m):
      if line[i] == ".":
         if shouldBeMoisted(i, m, previusLine, line, nextLine):
            line = line[:i] + "o" + line[i + 1:]

   for i in range(m - 1, -1, -1):
      if line[i] == ".":
         if shouldBeMoisted(i, m, previusLine, line, nextLine):
            line = line[:i] + "o" + line[i + 1:]

   return line

def shouldBeMoisted(i, m, previusLine, line, nextLine):
   if i == 0:
      return (
         previusLine[i] == "o" \
         or nextLine[i + 1] == "#" and line[i + 1] == "o"
      )
   elif i == m - 1:
      return (
         previusLine[i] == "o" \
         or nextLine[i - 1] == "#" and line[i - 1] == "o"
      )
   else:
      return (
         previusLine[i] == "o" \
         or nextLine[i - 1] == "#" and line[i - 1] == "o" \
         or nextLine[i + 1] == "#" and line[i + 1] == "o"
      )

main()

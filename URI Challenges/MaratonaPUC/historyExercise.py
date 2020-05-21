inputYears = []

while True:
   newLine = input()

   if newLine:
      inputYears.append(int(newLine))
   else:
      break

for year in inputYears:
   if (year % 100 == 0):
      print(year // 100)
   else:
      print((year // 100) + 1)

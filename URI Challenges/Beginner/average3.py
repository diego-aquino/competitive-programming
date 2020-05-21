def getWeightedAverage(arrayOfGrades):
   num1, num2, num3, num4 = arrayOfGrades[0], arrayOfGrades[1], arrayOfGrades[2], arrayOfGrades[3]

   return ((num1 * 2) + (num2 * 3) + (num3 * 4) + num4) / 10

def getStudentInExamStatus(initialAverage):
   examScore = float(input())

   print("Nota do exame: {}".format(examScore))

   newAverage = (initialAverage + examScore) / 2

   if (newAverage >= 5):
      print("Aluno aprovado.")
   else:
      print("Aluno reprovado.")

   print("Media final: {:.1f}".format(newAverage))

def printStudentStatus(grades):
   average = getWeightedAverage(grades)

   print("Media: {:.1f}".format(average))

   if (average >= 7):
      print("Aluno aprovado.")
   elif (average < 5):
      print("Aluno reprovado.")
   else:
      print("Aluno em exame.")

      getStudentInExamStatus(average)


def main():
   grades = input()

   grades = grades.split(" ")

   for i in range(len(grades)):
      grades[i] = float(grades[i])

   printStudentStatus(grades)


main()

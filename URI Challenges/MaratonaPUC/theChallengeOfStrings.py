S = input()
P = input()

q = int(input())

message = ""

for i in range(q):
   SArray = []

   for letter in S:
      SArray.append(letter)

   p, l = input().split()

   SArray[int(p) - 1] = l

   newS = "".join(SArray)

   message += str(newS.count(P)) + "\n"

print(message, end="")

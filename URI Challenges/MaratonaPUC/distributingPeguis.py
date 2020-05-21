inputData1 = input()
inputData2 = input()

inputData1 = inputData1.split(" ")

amountOfWorkers = int(inputData1[0])
workers = [0] * amountOfWorkers
steps = int(inputData1[1])

inputData2 = inputData2.split(" ")
pequis = []

for i in range(amountOfWorkers):
   pequis.append(int(inputData2[i]))

for step in range(steps):
   for i in range(amountOfWorkers):
      workers[i] += pequis[i]

   pequis.insert(0, pequis[amountOfWorkers - 1])
   pequis.pop(amountOfWorkers)

message = ""

for i in range(amountOfWorkers):
   message += "{}".format(workers[i])

   if i != amountOfWorkers - 1:
      message += " "

print(message)

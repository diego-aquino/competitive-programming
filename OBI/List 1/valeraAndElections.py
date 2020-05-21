def main():
   numberOfDistricts = int(input())
   roads = getRoads(numberOfDistricts)

   candidates = getCandidates(numberOfDistricts, roads)
   
   print("{}\n{}".format(len(candidates), " ".join(candidates)))

def getRoads(n):
   roads = []
   for i in range(n - 1):
      newRoad = input().split()

      for j in range(3):
         newRoad[j] = int(newRoad[j])
      
      roads.append(newRoad)
   
   return roads

def getCandidates(n, roads):
   roadsWithProblems = []
   for road in roads:
      if road[2] == 2:
         roadsWithProblems.append(road)

   for currentDistrict in range(n, 0, -1):
      


main()

def main():
   n, k = input().split()
   contestants = input().split()

   advanced = 0

   for contestantScore in contestants:
      if int(contestantScore) >= int(contestants[int(k) - 1]):
         if int(contestantScore) > 0:
            advanced += 1
      else: break

   print(advanced)

main()

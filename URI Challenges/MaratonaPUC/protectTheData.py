k = int(input())

speech = input()

tracks = []

i = -1

for character in speech:
   i += 1
   if character not in tracks:
      if speech.count(character) >= k:
         tracks.append(character)

j = -1

while True:
   j += 1

   newTracks = []

   for track in tracks:
      newTracks.append(track)

   for track in tracks:
      possibleTracks = []

      for showedUp in range(speech.count(track)):

         index = speech.index(track)

         possibleTrack = speech[index:index + j + 2]

         if speech.count(possibleTrack) >= k:
            if possibleTrack not in possibleTracks:
               possibleTracks.append(possibleTrack)


         possibleTrackArray = possibleTrack.split()

         if len(possibleTrackArray) > 1:
            speechSplitToWords = speech.split()

            possibleTrackArray.pop()
            possibleTrackJoined = " ".join(possibleTrackArray)

            if speechSplitToWords.count(possibleTrackJoined) > 1:
               firstIndex = speechSplitToWords.index(possibleTrackJoined)

               totalOccurrencesInARow = 1
               for x in range(speechSplitToWords.count(possibleTrackJoined)):
                  if len(speechSplitToWords) > firstIndex + 1:
                     if speechSplitToWords[firstIndex] == speechSplitToWords[firstIndex + 1]:
                        totalOccurrencesInARow += 1
                     else:
                        break
                  else:
                     break
                  firstIndex += 1

               if totalOccurrencesInARow >= k + 1:
                  position, correctCount = 0, 0

                  while position + k <= totalOccurrencesInARow:
                     correctCount += 1
                     position += 1

                  if correctCount >= k:
                     if possibleTrack not in possibleTracks:
                        possibleTracks.append(possibleTrack)

            else:
               if speech.count(possibleTrack) >= k:
                  if possibleTrack not in possibleTracks:
                     possibleTracks.append(possibleTrack)

      if len(possibleTracks) > 0:
         for validadedTrack in possibleTracks:
            if validadedTrack not in newTracks:
               newTracks.append(validadedTrack)

      newTracks.remove(track)

   if len(newTracks) > 0:
      tracks = newTracks
   else:
      break

if len(tracks) > 0:
   print(tracks[0])
else:
   print(":)")




# Para cada caractere, procurar outro igual e salvá-lo
# Para cada caractere igual encontrado, verificar quais dos outros tem o próximo
#   caractere igual a o dele e adicionar a um lista de posições de cada caractere
#   Ex.: "ab" -> "ab"
   # Ao final, apagar listas vazias
   # Repetir isso até verificar todos os trechos de caracteres iguais
# Verificar quais repetem pelo menos um número k de vezes, retirando da lista os
#   Os que não cumprem essa condição
# Imprimir na tela o primeiro trecho da lista
   # Se a lista for vazia, imprimir :)


def main():
    message = input()

    decodedMessage = ""

    for word in message.split():
        for i in range(len(word)):
            if i % 2 == 1:
                decodedMessage += word[i]

        decodedMessage += " "

    print(decodedMessage[:-1])

main()

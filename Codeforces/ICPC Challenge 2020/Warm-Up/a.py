from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    inputFile = open(askopenfilename(), "r")
    outputFile = open(asksaveasfilename(), "w")

    n = int(inputFile.readline())

    numbers = inputFile.readline().split()
    numbers.sort(key=(lambda x: int(x)))

    print(" ".join(numbers), file=outputFile)

    inputFile.close()
    outputFile.close()

main()

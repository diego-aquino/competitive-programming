from os import path, listdir

def main():
    root, publicTestsPath, testsPath = getPaths()

    writeClearPublicTestsFile(publicTestsPath)

    for folder in listdir(testsPath):
        inputSolutionPair = []
        
        for file in listdir(testsPath + folder):
            inputSolutionPair.append(open(testsPath + folder + "/" + file, "r"))

            if len(inputSolutionPair) == 2:
                writeTests(*inputSolutionPair, publicTestsPath)
                inputSolutionPair.clear()
            
def getPaths():
    root = path.dirname(path.abspath(__file__))
    publicTestsPath = root + "/public_tests.yaml"
    testsPath = root + "/tests/"

    return root, publicTestsPath, testsPath

def writeClearPublicTestsFile(path):
    publicTestsFile = open(path, "w")
    print("", file=publicTestsFile, end="")
    publicTestsFile.close()

def writeTests(inputFile, outputFile, publicTestsPath):
    publicTestsFile = prepateToWriteAtBottom(publicTestsPath)

    print("- input: |", file=publicTestsFile)
    for line in inputFile:
        print(" " * 4 + line, file=publicTestsFile, end="")

    print("  output: |", file=publicTestsFile)
    for line in outputFile:
        print(" " * 4 + line, file=publicTestsFile, end="")

    publicTestsFile.close()

def prepateToWriteAtBottom(publicTestsPath):
    publicTestsFile = open(publicTestsPath, "r")

    publicTestsContent = ""
    for line in publicTestsFile:
        publicTestsContent += line

    publicTestsFile.close()
    publicTestsFile = open(publicTestsPath, "w")

    print(publicTestsContent, file=publicTestsFile)

    return publicTestsFile

if __name__ == "__main__":
    main()

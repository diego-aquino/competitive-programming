from time import time

currentTime = 0
def startMeasuringTime():
    global currentTime
    currentTime = time()

def deltaTime():
    return '{:.20f}'.format(time() - currentTime)

# startMeasuringTime()
# print("OK 1")
# print(deltaTime())

# startMeasuringTime()
# print("OK 2")
# print(deltaTime())

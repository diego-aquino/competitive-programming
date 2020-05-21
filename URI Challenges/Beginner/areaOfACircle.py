pi = 3.14159

def getCircleArea(radius):
   return (pi * (radius ** 2))

R = float(input())
A = getCircleArea(R)

print("A=%.4f" % (A))
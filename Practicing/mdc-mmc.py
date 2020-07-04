def mdc(num1, num2):
    while True:
        remainder = num1 % num2
        num1, num2 = num2, remainder

        if remainder == 0:
            return num1

# mmc(a, b) = (a * b) / mdc(a, b)
def mmc(num1, num2):
    return num1 * num2 // mdc(num1, num2)

print(mmc(12, 15))

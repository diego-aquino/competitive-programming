def main():
    int(input())
    array = input().split()

    lines = ["", ""]

    for num in array:
        divisors = getDivisors(int(num))

        answer = solve(num, divisors, len(divisors))
        for i in range(2):
            lines[i] += str(answer[i]) + " "

    for i in range(2):
        print(lines[i][:-1])

def solve(num, divisors, m):
    for i in range(m):
        for j in range(i, m):
            if mdc(divisors[i] + divisors[j], int(num)) == 1:
                return (divisors[i], divisors[j])

    return (-1, -1)

def getDivisors(num):
    divisors = []

    for i in range(2, num + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors

def mdc(num1, num2):
    while True:
        remainder = num1 % num2
        num1, num2 = num2, remainder

        if remainder == 0: break

    return num1

main()

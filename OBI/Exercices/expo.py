def expo(num, power):
    if power == 1:
        return num
    else:
        x = expo(num, power // 2)

        if power % 2 == 0:
            return x * x
        else:
            return x * x * num

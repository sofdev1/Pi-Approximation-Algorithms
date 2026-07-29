def f():
    import cmath
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'
    print(Format.bold + Format.underline + "Borwein's Series" + Format.end)
    choose = input("""
Choose one of the following:
1. Class number 2
2. Class Number 4
""")

    a1 = 212175710912 * cmath.sqrt(61) + 1657145277365
    b1 = 13773980892672 * cmath.sqrt(61) + 107578229802750
    c1 = (5280 * (236674 + 30303 * cmath.sqrt(61))) ** 3

    a2 = 63365028312971999585426220 + 28337702140800842046825600 * cmath.sqrt(5) + (384
        * cmath.sqrt(5)
        * (10891728551171178200467436212395209160385656017
        + 4870929086578810225077338534541688721351255040 * cmath.sqrt(5)) ** 0.5)
    b2 = (7849910453496627210289749000
        + 3510586678260932028965606400 * cmath.sqrt(5)
        + 2515968
        * cmath.sqrt(3110)
        * (6260208323789001636993322654444020882161
        + 2799650273060444296577206890718825190235 * cmath.sqrt(5)) ** 0.5)
    c2 = (-214772995063512240
        - 96049403338648032 * cmath.sqrt(5)
        - 1296
        * cmath.sqrt(5)
        * (10985234579463550323713318473 + 4912746253692362754607395912 * cmath.sqrt(5))
        ** 0.5)

    exp1 = []
    exp2 = []

    if choose == "1":
        print("Class Number 2")
        m = int(input("Enter the number of terms (up to 11 only): "))

        for i in range(m):
            num1 = ((-1) ** i) * (math.factorial(6 * i)) * (a1 + i * b1)
            deno1 = (math.factorial(i) ** 3) * (math.factorial(3 * i)) * (c1 ** (i + 0.5))
            expression1 = num1 / deno1
            exp1.append(expression1)

        calculated1 = (1 / 12) * (sum(exp1) ** (-1))
        calculated = calculated1

    elif choose == "2":
        print("Class Number 4")
        n = int(input("Enter the number of terms (up to 6 only): "))

        for j in range(n):
            num2 = math.factorial(6 * j) * (a2 + j * b2)
            deno2 = math.factorial(3 * j) * (math.factorial(j) ** 3) * (c2 ** (3 * j))
            expression2 = num2 / deno2
            exp2.append(expression2)

        calculated2 = cmath.sqrt((-c2) ** 3) * (sum(exp2) ** (-1))
        calculated = calculated2

    print("Calculated value of pi is", calculated, "with an error of", abs((1 - (math.pi / calculated)) * 100), "%")

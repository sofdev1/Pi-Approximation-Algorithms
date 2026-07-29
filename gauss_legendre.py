def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'
    print(Format.bold + Format.underline + 'Gauss-Legendre Algorithm' + Format.end)
    n = int(input('Enter the number of iterations: '))
    a = 1
    b = 1/math.sqrt(2)
    t = 0.25
    p = 1
    for i in range(n):
        a_new = (a + b) / 2
        b = math.sqrt(a * b)
        t = t - p * ((a - a_new) ** 2)
        a = a_new
        p = p * 2
    calculated = ((a + b) ** 2) / (4 * t)
    print("Calculated value of pi is", calculated, "with an error of", abs((1 - (math.pi / calculated)) * 100), "%")

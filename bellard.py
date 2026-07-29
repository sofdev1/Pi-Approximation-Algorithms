def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + "Bellard's Formula" + Format.end)
    n = int(input('Enter the number of terms: '))

    total = 0.0
    for i in range(0, n):
        term1 = (-1) ** i / (2 ** (10 * i))
        term2 = (-2 ** 5) / (4 * i + 1)
        term3 = 1 / (4 * i + 3)
        term4 = 2 ** 8 / (10 * i + 1)
        term5 = 2 ** 6 / (10 * i + 3)
        term6 = 2 ** 2 / (10 * i + 5)
        term7 = 2 ** 2 / (10 * i + 7)
        term8 = 1 / (10 * i + 9)
        term = term1 * (term2 - term3 + term4 - term5 - term6 - term7 + term8)
        total += term

    calculated = (1 / (2 ** 6)) * total
    error = abs((1 - (math.pi / calculated)) * 100)

    print('Calculated value of pi is', calculated, 'with an error of', error, '%')

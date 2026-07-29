def f():
    import math

    class Format:
        end = '\033[0m'
        underline = '\033[4m'
        bold = '\033[1m'

    print(Format.bold + Format.underline + 'J. Munkhammar\'s Method' + Format.end)
    m = int(input('Enter the upper limit of the series: '))
    total = 0.0
    for i in range(1, m):
        term1 = 1 - ((i - 1) / m) ** 2
        term2 = 1 - (i / m) ** 2
        term = math.sqrt(((math.sqrt(term1) - math.sqrt(term2)) ** 2) + (m ** -2))
        total += term
    calculated = 2 * total
    print('Calculated value of pi is ', calculated, 'with an error of', abs((1 - (math.pi / calculated)) * 100), '%')
